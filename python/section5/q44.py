# -*- coding: utf-8 -*-
from graphviz import Digraph
from q41 import load_neko_chunk


def mkgraph(sentence, filename):
    g = Digraph(format='png')
    g.attr('node', shape='none')
    sg = Digraph('subgraph')
    sg.graph_attr.update(runk='same')
    for i in range(len(sentence) - 1):
        sg.edge(''.join(s.surface for s in sentence[i].morphs),
                ''.join(s.surface for s in sentence[i+1].morphs), color='#ffffff')

    for chunk in sentence:
        if chunk.dst != -1:
            src = ''.join(s.surface for s in chunk.morphs)
            dst = ''.join(s.surface for s in sentence[chunk.dst].morphs)
            g.edge(''.join(s.surface for s in chunk.morphs), ''.join(s.surface for s in sentence[chunk.dst].morphs))
    g.subgraph(sg)
    g.render(filename)

if __name__ == '__main__':
    document = load_neko_chunk()
    mkgraph(document[6], 'graph')
