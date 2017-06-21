# -*- coding: utf-8 -*-
from q40 import Morph


class Chunk:
    def __init__(self, dst):
        if type(dst) == str:
            dst = int(dst.replace('D', ''))
        self.dst = dst
        self.srcs = set()
        self.morphs = []

    def append(self, morph):
        if isinstance(self.morphs, tuple):
            print('cannot append')
        else:
            self.morphs.append(morph)

    def close(self):
        """morphsをこれ以上更新しない"""
        self.morphs = tuple(self.morphs)

    def open(self):
        """morphsを更新可能にする"""
        self.morphs = list(self.morphs)

    def append_src(self, src):
        self.srcs.add(int(src))

    def show(self):
        for morph in self.morphs:
            morph.show()
        print('_'*50)

    def show_surface(self, end='\n', key=None):
        for morph in filter(key, self.morphs):
            morph.show_surface(end='')
        print('', end=end)

    def filter_for_morph(self, key=None):
        return [] != [x for x in filter(key, self.morphs)]


def decide_srcs(chunks):
    for src, chunk in enumerate(chunks):
        dst = chunk.dst
        if dst > -1:
            chunks[dst].append_src(src)


def load_neko_chunk():
    nekopath = '../../data/neko.txt.cabocha'
    document = []
    sentence = []
    chunk = None
    for line in open(nekopath, 'r'):
        if '* ' == line[:2]:
            if chunk:
                chunk.close()
                sentence.append(chunk)
            _, _, dst, *_ = line.split(' ')
            chunk = Chunk(dst)
        elif 'EOS\n' == line:
            if chunk:
                sentence.append(chunk)
            chunk = None
            if sentence:
                decide_srcs(sentence)
                document.append(sentence)
                sentence = []
        else:
            surface, other = line.split('\t')
            pos, pos1, _, _, _, _, base, *_ = other.split(',')
            chunk.append(Morph(surface, base, pos, pos1))
    return document

if __name__ == '__main__':
    docu = load_neko_chunk()
    for i in (7, 8, 9):
        print(i)
        for chunk in docu[i]:
            chunk.show()
        print('\n\n', end='')
