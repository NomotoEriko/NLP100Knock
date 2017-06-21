# -*- coding: utf-8 -*-
from q50 import load_nlp


def load_in_word():
    sentences = load_nlp().split('\n')
    result = []
    for sentence in sentences:
        result.append('\n'.join(sentence.split()))
    return '\n\n'.join(result)

if __name__ == '__main__':
    print(load_in_word())
