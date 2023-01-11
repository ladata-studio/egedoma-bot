from words import words
from random import sample

def get_random_words(n = 4):
    indices = sample(range(0, len(words)), n)
    return (words[i] for i in indices)