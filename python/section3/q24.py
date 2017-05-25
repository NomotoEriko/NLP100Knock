# -*- coding: utf-8 -*-
from q20 import picup_eng_txt
import re


if __name__ == '__main__':
    txt = picup_eng_txt()
    pattern = r'\w+\.(png|jpg|mp3|svg)'
    media_list = set(m.group(0) for m in re.finditer(pattern, txt))
    print(media_list)
