# -*- coding: utf-8 -*-
from q20 import picup_eng_txt
import re


if __name__ == '__main__':
    txt = picup_eng_txt()
    pattern = r'\[\[Category:(\w+)\]\]'
    category_list = re.findall(pattern, txt)
    print(category_list)
