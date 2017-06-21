# -*- coding: utf-8 -*-
import xml.etree.ElementTree as et
import re
parse_pattern = re.compile(r'\([A-Z]+ ([^(]+?)\)')

def get_NP(sentence=None):
    if not sentence:
        print('input any sentence')
        return None
    print('sentence', sentence.attrib)
    [parse] = [p.text for p in sentence.iter('parse')]
    if not parse:
        print('has no parse')
        return None
    NP_idx = parse.index('(NP ')
    stack = 0
    words = []
    while True:
        idx = NP_idx+1
        stack += 1
        word = []
        while stack > 0:
            m = parse_pattern.search(parse[idx:])
            if not m:
                next_idx = len(parse)
            else:
                _, next_idx = m.span()
            next_idx += idx
            for c in parse[idx:next_idx]:
                if '(' == c:
                    stack += 1
                elif ')' == c:
                    stack -= 1
                    if stack == 0:
                        words.append(' '.join(word))
                        word = []
                        break
                    else:
                        pass
            idx = next_idx
            if stack > 0:
                word.append(m.group(1))
            else:
                stack = 0
                break
        if parse[NP_idx+4:].find('(NP ') != -1:
            NP_idx += parse[NP_idx+4:].find('(NP ')+4
        else:
            return words

if __name__ == '__main__':
    root = et.parse('../../data/nlp.txt.xml').getroot()
    target_sentence_id = (1, 2, 3, 4, 11)
    target_sentence = [s for s in root.findall('.//sentence')
                       if 'id' in s.attrib.keys() and int(s.attrib['id']) - 1 in target_sentence_id]
    for sentence in target_sentence:
        print(get_NP(sentence), end='\n\n')
