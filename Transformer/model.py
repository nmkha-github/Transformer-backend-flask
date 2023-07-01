import torch
from transformers import pipeline


class Model:
    def __init__(self):
        self.summarizer = None
        self.question_answering = None

    def load_model(self, task):
        try:
            if task == 'summarization':
                self.summarizer = pipeline(
                    'summarization', 'phongle1311/my_awesome_billsum_model')
            elif task == 'question-answering':
                self.question_answering = pipeline(
                    "question-answering", 'QuangHuy54/roberta-base-squad-1')
        except:
            print('$$$$$$$$$$$$$$$$$$ load model error ')
            return False

        return True

    def summarization(self, text):
        return self.summarizer(text)

    def question_answering(self, context, question):
        return self.question_answering(context=context, question=question)
