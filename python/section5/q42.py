# -*- coding: utf-8 -*-
from q41 import load_neko_chunk


def show_src_dst(document=None, nums=None):
    if not document:
        document = load_neko_chunk()
    if not nums:
        nums = range(len(document))

    for num in nums:
        print('-' * 50)
        print('sentence', num)
        print('係元\t係先')
        print('-'*50)
        sentence = document[num]
        for chunk in sentence:
            chunk.show_surface(end='\t', key=lambda x: x.pos!='記号')
            sentence[chunk.dst].show_surface(key=lambda x: x.pos!='記号')
        print('-'*50)


if __name__ == '__main__':
    show_src_dst(nums=[8, 9])
