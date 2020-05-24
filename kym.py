import os
from nltk.stem.snowball import SnowballStemmer

from training_data import TrainingData
from sentence import Sentence

stemmer = SnowballStemmer(language="portuguese")

# Fatorar os metodos
# Fazer filter
# Econtrar argumentos

class Kym:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = TrainingData(self.data_path)

        self.data.load()

    def handle_sentence(self, string):
        sentence = Sentence(string, self.data)

        if(math := sentence.math):
            return math

        return sentence.arguments
        