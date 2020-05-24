import spacy
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer(language="portuguese")
nlp = spacy.load("pt_core_news_sm")

"""
    melhorar a funçao cal...
"""

class Sentence:
    def __init__(self, string, data):
        self.data = data

        self.string = string
        self.tokenized = nlp(string)

        self.better_class = self.calculate_best_class()
        self.arguments = self.catch_arguments()

        self.math = self.__test_math()

    def calculate_best_class(self):
        score = 0

        word_frequency = self.data.words_frequency
        words_in_class = self.data.words_in_class
        classes = self.data.classes

        better_class = {"class":None, "score":0}

        for class_name in classes:
            class_name = class_name.name

            for word in self.string.split():
                word = stemmer.stem(word.lower())

                if(word in words_in_class[class_name]):
                    currentScore = (1 / word_frequency[word])
                    score += currentScore

                    if(score > better_class['score']):
                        better_class['class'] = class_name
                        better_class['score'] = score

        return better_class

    def __test_math(self):
        try:
            return eval(self.string)
        except:
            return None

    def catch_arguments(self):
        classes = self.data.classes
        words_frequency = self.data.words_frequency
        print("1: ", words_frequency)


        most_frequently = None

        for class_name in classes:
            class_name = class_name.name

            print("2: ", most_frequently)

        return most_frequently

