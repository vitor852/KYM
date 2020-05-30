from functions.microphone import listen_microphone
from kym import Kym
from sentence import Sentence
import pandas as pd

import sys
import os

training_data_path = "C:/Users/vitor/Documents/KYM/src/database/traindata.csv"
test_data_path = "C:/Users/vitor/Documents/KYM/src/test.txt"

kym = Kym(data_path=training_data_path)
kym.init()


if __name__ == "__main__":
    resp = None

    
    for test in pd.read_csv(test_data_path)["sentences"]:
        # sentence = listen_microphone()
        # sentence = Sentence(sentence)

        resp = Sentence([test], kym)
        print(test, resp.label)