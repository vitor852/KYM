from file import File
from os import path
import os
import nltk
from nltk.stem.snowball import SnowballStemmer

"""
    # Carregar classes
    # Tratar os dados para treinamento
"""

# Implementar erro caso diretorio recebido não seja valido

stemmer = SnowballStemmer(language="portuguese")

class TrainingData():
    def __init__(self, path):
        self.path = path

        self.classes = []
        self.train_data = []

        self.words_in_class = {}
        self.words_frequency = {}

    def load(self):
        self.__load_classes()
        self.__load_data()
        self.__arrange_data()

    def __load_classes(self):
        file = File(self.path + 'classes.txt')

        for class_path in file.read_file():
            temp = path.join(self.path, class_path)

            for class_name in os.listdir(temp):
                f = path.join(temp, class_name)
                class_file = File(f)

                self.classes.append(class_file)

    def __load_data(self):
        for file in self.classes:
            for line in file.read_file():
                if(line):
                    sentence = line.strip()
                    self.train_data.append({"class":file.name, "sentence":sentence})

    def __arrange_data(self):
        for c in self.classes:
            class_name = c.name
            self.words_in_class[class_name] = []
            self.words_frequency[class_name] = []

        for data in self.train_data:
            sentence = nltk.word_tokenize(data['sentence'])

            for _, word in enumerate(sentence):
                if(word not in '()'):
                    stemmed_word = stemmer.stem(word.lower())

                    if(stemmed_word not in self.words_frequency):
                        self.words_frequency[stemmed_word] = 1
                    else:
                        self.words_frequency[stemmed_word] += 1

                    self.words_in_class[data['class']].extend([stemmed_word])