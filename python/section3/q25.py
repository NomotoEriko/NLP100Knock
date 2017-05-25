# -*- coding: utf-8 -*-
from q20 import picup_eng_txt
import re
from pprint import pprint

if __name__ == '__main__':
    txt = picup_eng_txt()
    txt = txt[txt.find('{{基礎情報 国'):]
    txt = txt.split('\n')[1:]
    pattern = re.compile(r'\|(\w+) = ([^{]+)')
    pattern2 = re.compile(r'\|(\w+) = {{(\w+)')
    line = txt.pop(0)
    m = re.match(pattern, line)
    infomation_list = {}
    while m:
        infomation_list[m.group(1)] = re.sub(r'<[^>]*>', '', m.group(2))
        line = txt.pop(0)
        m = re.match(pattern, line)
        if not m:
            m2 = re.match(pattern2, line)
            if m2:
                v = ''
                line = txt.pop(0)
                m = re.match(pattern, line)
                while not m:
                    v += re.sub(r'<[^>]*>', '', line.strip())
                    line = txt.pop(0)
                    m = re.match(pattern, line)
                infomation_list[m2.group(1)] = v

    pprint(infomation_list)
