# -*- coding: utf-8 -*-
import xml.etree.ElementTree as et


def load_xml_in_word_lemma_pos_1(path='../../data/nlp.txt.xml'):
    tree = et.parse(path)
    root = tree.getroot()
    words = root.findall('.//word')
    lemmas = root.findall('.//lemma')
    poses = root.findall('.//POS')
    return '\n'.join('\t'.join(e.text for e in wlp) for wlp in zip(words, lemmas, poses))


def load_xml_in_word_lemma_pos_2(path='../../data/nlp.txt.xml'):
    tree = et.parse(path)
    root = tree.getroot()
    tokens = root.findall('.//token')
    return '\n'.join('\t'.join((t.find('./word').text, t.find('./lemma').text, t.find('./POS').text)) for t in tokens)


if __name__ == '__main__':
    print(load_xml_in_word_lemma_pos_1()[:100], end='\n\n')
    print(load_xml_in_word_lemma_pos_2()[:100])
