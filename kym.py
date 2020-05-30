import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

language = "portuguese"
stemmer = SnowballStemmer(language)
stopwords = [stop for stop in stopwords.words(language)]
vectorizer = CountVectorizer()

# Fatorar os metodos
# Fazer filter
# Econtrar argumentos

class Kym:
    def __init__(self, data_path):
        self.model = GaussianNB()
        self.encoder = LabelEncoder()

        self.train_data = pd.read_csv(data_path)
        self.train_sentences = self.train_data["sentences"]
        self.train_labels = self.encoder.fit_transform([label for label in self.train_data["labels"]])
        self.train_arguments = self.train_data["arguments"]

        self.train_matrix = None
        self.data_dict = None
        self.processed_data = None

        self.kym = self

    def init(self):
        self.processed_data = self.pre_process_data(self.train_sentences)
        self.data_dict = vectorizer.fit(self.processed_data).vocabulary_
        self.train_matrix = self.extract_features(self.processed_data)

        self.model.fit(self.train_matrix, self.train_labels)

    def pre_process_data(self, data):
        sentences = [sentence for sentence in data]
        processed_sentences = []
        
        for sentence in sentences:
            processed_sentence = ""
            for word in word_tokenize(sentence):
                if(word.isalpha()):
                    processed_sentence += f" {stemmer.stem(word)}"

            processed_sentence = processed_sentence.strip()
            processed_sentences.append(processed_sentence)

        return processed_sentences

    def extract_features(self, data):
        data_matrix = np.zeros((len(data), len(self.data_dict)))

        for index, sentence in enumerate(data):
            sentence = word_tokenize(sentence)
            for word in sentence:
                try:
                    data_matrix[index, self.data_dict[word]] = 1
                except:
                    pass

        return data_matrix