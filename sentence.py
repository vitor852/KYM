class Sentence:
    def __init__(self, sentence, Kym):
        self.text = sentence
        self.processed_sentence = Kym.pre_process_data(sentence)
        self.sentence_matrix = Kym.extract_features(self.processed_sentence)
        self.label = Kym.model.predict(self.sentence_matrix)
        self.label = Kym.encoder.inverse_transform(self.label)