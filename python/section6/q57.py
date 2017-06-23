# -*- coding: utf-8 -*-
from graphviz import Digraph
import xml.etree.ElementTree as et


def get_graph(sentence=None, name='graph', comment='', format='svg'):
    if not sentence:
        return None
    if not sentence.find('./tokens'):
        print('has no tokens')
        return None
    if not sentence.find('./dependencies'):
        print('has no dependencies')
        return None
    tokens = [t for t in sentence.findall('./tokens/token') if 'id' in t.attrib.keys()]
    dependencies = [d for d in sentence.findall('./dependencies') if d.attrib['type'] == "collapsed-dependencies"][0]
    dependencies = [d for d in dependencies.findall('./dep') if 'type' in d.attrib.keys()]

    name += str(int(sentence.attrib['id'])-1)
    graph = Digraph(name=name, format=format, comment=comment)
    with graph.subgraph(name='tmp') as c:
        c.attr('node', shape='plaintext')
        c.attr('edge', color='white')
        c.edge(' ', '')
    with graph.subgraph(name='sub') as sub:
        sub.attr('node', shape='plaintext')
        sub.attr(rankdir='LR')
        sub.attr(rank='same')
        tsurface = 'ROOT'
        tidx = '0'
        sub.node(tidx, tsurface)
        sub.edge('', tidx, color='white')
        edges = []
        for token in sorted(tokens, key=lambda x: int(x.attrib['id'])):
            idx = token.attrib['id']
            surface = token.find('./word').text
            edges.append([tidx, idx])
            tsurface = surface
            tidx = idx
            sub.node(tidx, tsurface)
        sub.attr('edge', color='white', shape='rarrow', weight='1')
        sub.edges(edges)

    graph.attr('edge', shape='narrow', splines='ortho', weight='0')
    for dep in dependencies:
        governer = dep.find('./governor').attrib['idx']
        dependent = dep.find('./dependent').attrib['idx']
        label = dep.attrib['type']
        # graph.attr('edge', weight='0')
        graph.edge(governer, dependent)

    graph.render(name)
    print(name)

if __name__ == '__main__':
    root = et.parse('../../data/nlp.txt.xml').getroot()
    target_sentence_id = (0, 1, 8,)
    target_sentence = [s for s in root.findall('.//sentences/sentence')
                       if 'id' in s.attrib.keys() and int(s.attrib['id']) - 1 in target_sentence_id]
    for sentence in target_sentence:
        print(get_graph(sentence))
