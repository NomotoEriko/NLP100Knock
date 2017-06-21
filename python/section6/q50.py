# -*- coding: utf-8 -*-
import re


def load_nlp():
    sentence_pattern = re.compile(r'[,.!?]\s[A-Z]')
    sentences = []
    for line in open('../../data/nlp.txt', 'r'):
        m = re.search(sentence_pattern, line)
        while m:
            sentence = line[:m.start() + 1].strip()
            if len(sentence) > 0:
                sentences.append(sentence)
            line = line[m.start()+1:]
            m = re.search(sentence_pattern, line)
        line = line.strip()
        if len(line) > 0:
            sentences.append(line)
    return '\n'.join(sentences)


if __name__ == '__main__':
    print(load_nlp())
