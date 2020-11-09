import nltk
import pickle
import os.path
from collections import Counter

class Vocabulary(object):

    def __init__(self,
                 vocab_file='./src/models/vocab.pkl',
                 vocab_from_file=True):
        self.vocab_file = vocab_file
        self.vocab_from_file = vocab_from_file
        self.get_vocab()

    def get_vocab(self):
        """Load the vocabulary from file OR build the vocabulary from scratch."""
        if os.path.exists(self.vocab_file) & self.vocab_from_file:
            f = open(self.vocab_file, "rb")
            vocab = pickle.load(f)
            self.word2idx = vocab.word2idx
            self.idx2word = vocab.idx2word
            f.close()
        else:
            self.build_vocab()
            with open(self.vocab_file, 'wb') as f:
                pickle.dump(self, f)

    def __len__(self):
        return len(self.word2idx)