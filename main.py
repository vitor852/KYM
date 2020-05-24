from functions.microphone import listen_microphone
from kym import Kym
from sentence import Sentence

import sys
import os

training_data_path = "C:/Users/vitor/Documents/KYM/src/database/"
test_data_path = "C:/Users/vitor/Documents/KYM/src/test.txt"

kym = Kym(training_data_path)

def load_test_data():
    test_data = []

    with open(test_data_path) as file:
        for line in file.readlines():
            if(line != '\n'):
                line = line.strip()
                test_data.append(line)

    return test_data


if __name__ == "__main__":
    resp = None

    if(sys.argv[1]):
        resp = kym.handle_sentence(sys.argv[1])
        print(resp)
    else:
        for test in load_test_data():
            # sentence = listen_microphone()
            # sentence = Sentence(sentence)

            resp = kym.handle_sentence(test)
            print(resp)