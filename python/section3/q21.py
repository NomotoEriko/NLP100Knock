# -*- coding: utf-8 -*-
from q20 import picup_eng_txt
import re


if __name__ == '__main__':
    txt = picup_eng_txt().split('\n')
    pattern = r'\[\[Category:(\w+)\]\]'
    categpry_list = [t for t in filter(lambda x: re.search(pattern, x[1]) != None, enumerate(txt))]
    print(categpry_list)
