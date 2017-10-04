# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs


def get_国名リスト():
    soup = bs(requests.get('https://en.wikipedia.org/wiki/List_of_sovereign_states').text, "html5lib")
    table = soup.table
    trs = table.find_all('tr')[3:]
    return set([e.a.text for e in trs if e.a])


def replace_one_国名(国名, lines):
    if ' ' in 国名:
        new_国名 = 国名.replace(' ', '_')
        return [line.replace(国名, new_国名) for line in lines]
    else:
        return lines


def replace_国名(国名リスト, lines):
    for 国名 in 国名リスト:
        lines = replace_one_国名(国名, lines)
    return lines


def main(data='q80.txt'):
    lines = [line for line in open(data)]
    国名リスト = get_国名リスト()
    lines = replace_国名(国名リスト, lines)
    with open('q81.txt', 'w') as f:
        f.write(''.join(lines))

if __name__ == '__main__':
    main()
