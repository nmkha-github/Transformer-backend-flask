import torch
from transformers import pipeline


class Transformer:
    def __init__(self):
        self.summarizer = None

    def load_model(self):
        try:
            self.summarizer = torch.load('Transformer/m.pkl')
        except:
            print('$$$$$$$$$$$$$$$$$$ load model error ')
            return False

        return True

    def summarize(self, text):
        return self.summarizer(text)
