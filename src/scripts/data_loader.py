import os
import torch.utils.data as data
from vocabulary import Vocabulary
from PIL import Image
import numpy as np
import json

def get_loader(transform, mode='dev', batch_size=1, vocab_file='./src/models/vocab.pkl',
               vocab_from_file=True, num_workers=0):

    if mode == 'dev':
        assert batch_size == 1, "Please change batch_size to 1 if testing your model."
        assert os.path.exists(vocab_file), "Must first generate vocab.pkl from training data."
        assert vocab_from_file == True, "Change vocab_from_file to True."
        img_folder = "./src/images/"
        display_file = "./src/misc/display.json"
    dataset = Dataset(transform=transform, mode=mode, batch_size=batch_size, vocab_file=vocab_file,
                      display_file=display_file, vocab_from_file=vocab_from_file, img_folder=img_folder)
    data_loader = data.DataLoader(dataset=dataset,
                                  batch_size=dataset.batch_size,
                                  shuffle=True,
                                  num_workers=num_workers)

    return data_loader

class Dataset(data.Dataset):
    def __init__(self, transform, mode, batch_size, vocab_file, display_file, vocab_from_file, img_folder):
        self.transform = transform
        self.mode = mode
        self.batch_size = batch_size
        self.vocab = Vocabulary(vocab_file, vocab_from_file)
        self.img_folder = img_folder
        test_info = json.loads(open(display_file).read())
        self.paths = [item['file_name'] for item in test_info['images']]

    def __getitem__(self, index):
        path = self.paths[index]
        PIL_image = Image.open(os.path.join(self.img_folder, path)).convert('RGB')
        orig_image = np.array(PIL_image)
        image = self.transform(PIL_image)
        return orig_image, image

    def __len__(self):
        return len(self.paths)