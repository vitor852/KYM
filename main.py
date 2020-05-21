from functions.microphone import listen_microphone
from kym import Kym
from sentence import Sentence

import os

training_data_path = "/home/vitor/Documentos/projetos/kym/src/database/"
test_data_path = os.path.join("/home/vitor/Documentos/projetos/kym/src/test.txt")

kym = Kym(training_data_path)
kym.init()

def load_test_data():
    test_data = []

    with open(test_data_path) as file:
        for line in file.readlines():
            if(line != '\n'):
                line = line.strip()
                test_data.append(line)

    return test_data


if __name__ == "__main__":
    for test in load_test_data():
        # sentence = listen_microphone()
        # sentence = Sentence(sentence)

        sentence = Sentence(test)

        print(f"{Sentence.better_class}\n")