# -*- coding: utf-8 -*-
from graphviz import Digraph
from q41 import load_neko_chunk


def mkgraph(sentence, filename):
    g = Digraph(format='png')
    g.attr('node', shape='circle')
    for chunk in sentence:
        if chunk.dst != -1:
            src = ''.join(s.surface for s in chunk.morphs)
            dst = ''.join(s.surface for s in sentence[chunk.dst].morphs)
            g.edge(''.join(s.surface for s in chunk.morphs), ''.join(s.surface for s in sentence[chunk.dst].morphs))
    g.render(filename)

if __name__ == '__main__':
    document = load_neko_chunk()
    mkgraph(document[6], 'graph')
