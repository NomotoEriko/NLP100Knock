# -*- coding: utf-8 -*-
import xml.etree.ElementTree as et


def get_SVO(sentence=None):
    """
    :param sentence:
    :return: sentence_id, S_surface, V_surface, O_surface
    """
    if not sentence:
        print('input any sentence')
        return None
    if not sentence.find('./tokens'):
        print('has no tokens')
        return None
    print('sentence', sentence.attrib)
    [dependencies] = [d for d in sentence.iter('dependencies') if d.attrib['type'] == "collapsed-dependencies"]
    # dependencies = [d for ...][0]ではchildが消えた。上記のように書くとうまくいった。
    if not dependencies:
        # if not dependencies:でdependenciesにElementオブジェクトが入っていても何故かこの中に入る。
        # コンソールだと入らない。意味がわからないよ！！
        # ↑childがないから
        print(dependencies)
        print('has no dependencies')
        return None
    nsubi = []
    dobj = []
    for dep in dependencies.iter('dep'):
        tag = dep.attrib['type']
        if 'nsubj' in tag:
            nsubi.append(dep)
        elif 'dobj' == tag:
            dobj.append(dep)
        else:
            pass
    V = (set((g.find('governor').attrib['idx'], g.find('governor').text) for g in nsubi)
         & set((g.find('governor').attrib['idx'], g.find('governor').text) for g in dobj))
    if V:
        V = V.pop()
        [S] = [g.find('dependent').text for g in nsubi if V[0] == g.find('governor').attrib['idx']]
        [O] = [g.find('dependent').text for g in dobj if V[0] == g.find('governor').attrib['idx']]
        return '\t'.join((S, V[1], O))
    else:
        return 'has no V'

if __name__ == '__main__':
    root = et.parse('../../data/nlp.txt.xml').getroot()
    target_sentence_id = (1, 2, 3, 4, 11)
    target_sentence = [s for s in root.findall('.//sentence')
                       if 'id' in s.attrib.keys() and int(s.attrib['id']) - 1 in target_sentence_id]
    for sentence in target_sentence:
        print(get_SVO(sentence), end='\n\n')
