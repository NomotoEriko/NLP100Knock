# -*- coding: utf-8 -*-
from q20 import picup_eng_txt
import re
from pprint import pprint


def get_rid_of_strong_markup(txt):
    txt = re.sub(r"('+)([^']+)\1", r'\2', txt)
    return txt


def mk_information():
    txt = picup_eng_txt()
    txt = re.search(r'{{基礎情報.+?}}\n', txt, flags=re.DOTALL).group(0)
    txt = txt.split('\n')[1:]
    pattern = re.compile(r'\|(\w+) = ([^{]+)')
    pattern2 = re.compile(r'\|(\w+) = {{(\w+)')
    line = txt.pop(0)
    m = re.match(pattern, line)
    infomation_list = {}
    while m:
        infomation_list[m.group(1)] = get_rid_of_strong_markup(m.group(2))
        line = txt.pop(0)
        m = re.match(pattern, line)
        if not m:
            m2 = re.match(pattern2, line)
            if m2:
                v = ''
                line = txt.pop(0)
                m = re.match(pattern, line)
                while not m:
                    v += get_rid_of_strong_markup(line)
                    line = txt.pop(0)
                    m = re.match(pattern, line)
                infomation_list[m2.group(1)] = v
    return infomation_list


if __name__ == '__main__':
    txt = picup_eng_txt()
    txt = re.search(r'{{基礎情報.+?}}\n', txt, flags=re.DOTALL).group(0)
    txt = txt.split('\n')[1:]
    pattern = re.compile(r'\|(\w+) = ([^{]+)')
    pattern2 = re.compile(r'\|(\w+) = {{(\w+)')
    line = txt.pop(0)
    m = re.match(pattern, line)
    infomation_list = {}
    while m:
        infomation_list[m.group(1)] = get_rid_of_strong_markup(m.group(2))
        line = txt.pop(0)
        m = re.match(pattern, line)
        if not m:
            m2 = re.match(pattern2, line)
            if m2:
                v = ''
                line = txt.pop(0)
                m = re.match(pattern, line)
                while not m:
                    v += get_rid_of_strong_markup(line)
                    line = txt.pop(0)
                    m = re.match(pattern, line)
                infomation_list[m2.group(1)] = v
    pprint(infomation_list)
