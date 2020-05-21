import os
from training_data import TrainingData
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer(language="portuguese")

# Fatorar os metodos
# Fazer filter
# Econtrar argumentos

class Kym:
    def __init__(self, data_path):
        self.data = TrainingData(data_path)

    def init(self):
        self.data.load()

    def calculate_best_class(self, sentence):
        score = 0

        word_frequency = self.data.word_frequency
        words_in_class = self.data.words_in_class
        classes = self.data.classes

        better_class = {"class":None, "score":0}

        for class_name in classes:
            for word in sentence.tokenized:
                word = stemmer.stem(word.lower())

                if(word in words_in_class[class_name]):
                    currentScore = (1 / word_frequency[word])
                    score += currentScore

                    if(score > better_class['score']):
                        better_class['class'] = class_name
                        better_class['score'] = score

        return better_class