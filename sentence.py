# import nltk
from kym import Kym
import spacy
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer(language="portuguese")
nlp = spacy.load("pt_core_news_sm")

class Sentence:
    def __init__(self, string):
        self.tokenized = nlp(string)
        self.better_class = Kym.calculate_best_class("o que é")