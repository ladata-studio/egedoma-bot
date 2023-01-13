from words import short_words
from random import sample

def get_random_words(n = 4):
    indices = sample(range(0, len(short_words)), n)
    return (short_words[i] for i in indices)
