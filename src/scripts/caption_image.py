from torchvision import transforms
import os
import json
import torch
from src.scripts.model import EncoderCNN, DecoderRNN
from src.scripts.data_loader import get_loader
import re


def define_device():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    return device


def create_transform_test():
    transform_test = transforms.Compose([
        transforms.Resize(256),                         # smaller edge of image resized to 256
        transforms.RandomCrop(224),                     # get 224x224 crop from random location
        transforms.RandomHorizontalFlip(),              # horizontally flip image with probability=0.5
        transforms.ToTensor(),                          # convert the PIL Image to a tensor
        transforms.Normalize((0.485, 0.456, 0.406),     # normalize image for pre-trained model
                             (0.229, 0.224, 0.225))])

    return transform_test


def create_data_loader(transform, mode):
    data_loader = get_loader(transform=transform, mode=mode)
    return data_loader


def get_sample_image(data_loader):
    orig_image, image = next(iter(data_loader))
    return orig_image, image


def create_nn(device, vocab_size, embed_size, hidden_size,
              encoder_file, decoder_file, models_dir="./src/models"):
    encoder = EncoderCNN(embed_size)
    encoder.eval()
    decoder = DecoderRNN(embed_size, hidden_size, vocab_size)
    decoder.eval()
    encoder.load_state_dict(torch.load(os.path.join(models_dir, encoder_file), map_location=device))
    decoder.load_state_dict(torch.load(os.path.join(models_dir, decoder_file), map_location=device))
    encoder.to(device)
    decoder.to(device)

    return encoder, decoder


def exec_decoder_sampler(device, data_loader, image, encoder, decoder):
    image = image.to(device)
    features = encoder(image).unsqueeze(1)
    output = decoder.sample(features)
    assert (type(output) == list), "Output needs to be a Python list"
    assert all([type(x) == int for x in output]), "Output should be a list of integers."
    assert all([x in data_loader.dataset.vocab.idx2word for x in
                output]), "Each entry in the output needs to correspond to an integer that indicates a token in the vocabulary."

    return output


def clean_sentence(sampled_ids, vocab):
    sampled_caption = []
    for word_id in sampled_ids:
        word = vocab.idx2word[word_id]
        sampled_caption.append(word)
        if word == "<end>":
            break
    s = ' '.join(sampled_caption)
    pattern = "<start>(.*?)<end>"
    sentence = re.search(pattern, s).group(1)

    return sentence


def get_prediction(device, data_loader, vocab, encoder, decoder):
    try:
        orig_image, image = next(iter(data_loader))
        image = image.to(device)
        features = encoder(image).unsqueeze(1)
        output = decoder.sample(features)
        new_caption = clean_sentence(output, vocab)
    except Exception as e:
        new_caption = "not sure what this is . please upload another image ."

    return new_caption


def save_display(image_name):
    img_id = int(image_name.split(".")[0].split("_")[-1])
    d = {"images":[{
      "file_name": image_name,
      "id": img_id
    }]}
    jstr = json.dumps(d)
    file = open("./src/misc/display.json", "w")
    file.write(jstr)
    file.close()


def run(image_name):
    save_display(image_name)
    encoder_file = "encoder-5.pkl"
    decoder_file = "decoder-5.pkl"
    embed_size = 256
    hidden_size = 512
    device = define_device()
    transform_test = create_transform_test()
    data_loader = create_data_loader(transform_test, mode='dev')
    vocab = data_loader.dataset.vocab
    vocab_size = len(vocab)
    encoder, decoder = create_nn(device, vocab_size, embed_size, hidden_size, encoder_file, decoder_file)
    new_caption = get_prediction(device, data_loader, vocab, encoder, decoder)

    return new_caption