# -*- coding: utf-8 -*-
from pprint import pprint

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def show(self, end='\n'):
        print('{0:>10} {1:>10} {2:>10} {3:>10}'.format(self.surface, self.base, self.pos, self.pos1), end=end)

    def show_surface(self, end='\n'):
        print(self.surface, end=end)

    def show_base(self, end='\n'):
        print(self.base, end=end)

    def show_pos(self, end='\n'):
        print(self.pos, end=end)

    def show_pos1(self, end='\n'):
        print(self.pos1, end=end)


def load_neko_morph():
    nekopath = '../../data/neko.txt.cabocha'
    document = []
    sentence = []
    for line in open(nekopath, 'r'):
        if '* ' == line[:2]:
            pass
        elif 'EOS\n' == line:
            if sentence:
                document.append(sentence)
                sentence = []
        else:
            surface, other = line.split('\t')
            pos, pos1, _, _, _, _, base, *_ = other.split(',')
            sentence.append(Morph(surface, base, pos, pos1))
    return document


def show_morphs(document, sentence_nums):
    for num in sentence_nums:
        sentense = document[num]
        print(num, end=':')
        for morph in sentense:
            morph.show()
        print('\n\n', end='')


if __name__ == '__main__':
    show_morphs(load_neko_morph(), [2, 3, 4])
