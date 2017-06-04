# -*- coding: utf-8 -*-
from q41 import load_neko_chunk
from pprint import pprint


def noun_to_root(sentence):
    nouns = [chunk for chunk in filter(lambda chunk: chunk.filter_for_morph(lambda m:m.pos == '名詞'), sentence)]
    for noun in nouns:
        print(''.join(m.surface for m in filter(lambda x: x.pos != '記号', noun.morphs)), end='')
        dst = noun.dst
        while dst != -1:
            print(' –> ' + ''.join(m.surface for m in filter(lambda x: x.pos != '記号', sentence[dst].morphs)), end='')
            dst = sentence[dst].dst
        print('')


if __name__ == '__main__':
    document = load_neko_chunk()
    for i in 8, 9, 10:
        print(i)
        noun_to_root(document[i])
