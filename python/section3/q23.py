# -*- coding: utf-8 -*-
from q20 import picup_eng_txt
import re

if __name__ == '__main__':
    txt = picup_eng_txt()
    pattern = r'(=+)(\w+)\1'
    section_list = re.findall(pattern, txt)
    # section_list = [(section_name, section_level), ... ]
    section_list = [(x[1], len(x[0])-1) for x in section_list]
    print(section_list)
