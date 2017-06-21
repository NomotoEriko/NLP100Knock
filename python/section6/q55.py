# -*- coding: utf-8 -*-
import xml.etree.ElementTree as et


def xml_person(path='../../data/nlp.txt.xml'):
    tree = et.parse(path)
    root = tree.getroot()
    for token in root.findall('.//token'):
        a = token.find('./NER').text
        b = a=='O'
    persons = [t.find('./word').text for t in filter(lambda x: x.find('./NER').text == 'PERSON', root.findall('.//token'))]
    return set(persons)

if __name__ == '__main__':
    print('\n'.join(xml_person()))
