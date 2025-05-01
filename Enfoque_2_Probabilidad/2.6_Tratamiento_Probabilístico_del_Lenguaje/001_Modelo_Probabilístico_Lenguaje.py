import re
from collections import defaultdict

class BigramModel:
    def __init__(self):
        self.model = defaultdict(lambda: defaultdict(int))

    def tokenize(self, text):
        # Limpia el texto y separa palabras
        text = re.sub(r'[^\w\s]', '', text.lower())
        return text.split()

    def train(self, corpus):
        tokens = self.tokenize(corpus)
        for i in range(len(tokens) - 1):
            self.model[tokens[i]][tokens[i+1]] += 1

    def predict_next(self, word):
        next_words = self.model[word]
        if not next_words:
            return None
        # Devuelve la palabra más probable que sigue a 'word'
        return max(next_words, key=next_words.get)
