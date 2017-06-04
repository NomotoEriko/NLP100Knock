# -*- coding: utf-8 -*-
from q41 import load_neko_chunk


def show_noun_varb(document=None, nums=None, details='on'):
    if not document:
        document = load_neko_chunk()
    if not nums:
        nums = range(len(document))
    for num in nums:
        if 'on' == details:
            print('-' * 50)
            print('sentence', num)
            print('名詞を含む係元\t動詞を含む係先')
            print('-'*50)
        sentence = document[num]
        for chunk in sentence:
            if chunk.filter_for_morph(lambda x: x.pos == '名詞') and \
                    sentence[chunk.dst].filter_for_morph(lambda x: x.pos in '動詞'):
                chunk.show_surface(end='\t', key=lambda x: x.pos != '記号')
                sentence[chunk.dst].show_surface(end='\n', key=lambda x: x.pos != '記号')
        if 'on' == details:
            print('-' * 50)


if __name__ == '__main__':
    show_noun_varb(nums=[8, 9], details='off')
