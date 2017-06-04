# -*- coding: utf-8 -*-
from q41 import load_neko_chunk


def i_to_j(sentence, i, j):
    """
    this function calculate i to j path.
    :param sentence: chunk list
    :param i: noun_chunk idx (smaller)
    :param j: noun_chunk idx (bigger)
    :return: i to j path string
    """
    i_surface = ''.join('X' if m.pos == '名詞' else m.surface
                        for m in filter(lambda x: x.pos != '記号', sentence[i].morphs))
    j_surface = ''.join('Y' if m.pos == '名詞' else m.surface
                        for m in filter(lambda x: x.pos != '記号', sentence[j].morphs))
    i_to_root = []
    dst = sentence[i].dst
    while dst != -1:
        i_to_root.append(dst)
        dst = sentence[dst].dst
    if j in i_to_root:
        i_to_j_idx = i_to_root[:i_to_root.index(j)]
        i_to_j_surface = [''.join(m.surface for m in filter(lambda x: x.pos != '記号', sentence[idx].morphs))
                          for idx in i_to_j_idx]
        surfaces = [i_surface] + i_to_j_surface + [j_surface]
        return ' –> '.join(surfaces)
    else:
        j_to_root = []
        dst = sentence[j].dst
        while dst != -1:
            j_to_root.append(dst)
            dst = sentence[dst].dst
        intersection = -1
        for idx in i_to_root:
            if idx in j_to_root:
                intersection = idx
                break

        # i_to_intersection
        i_to_intersection = i_to_root[:i_to_root.index(intersection)]
        i_to_intersection_surface = [''.join(m.surface for m in filter(lambda x: x.pos != '記号', sentence[idx].morphs))
                                     for idx in i_to_intersection]
        i_to_intersection_surface = [i_surface] + i_to_intersection_surface

        # j_to_intersection
        j_to_intersection = j_to_root[:j_to_root.index(intersection)]
        j_to_intersection_surface = [''.join(m.surface for m in filter(lambda x: x.pos != '記号', sentence[idx].morphs))
                                     for idx in j_to_intersection]
        j_to_intersection_surface = [j_surface] + j_to_intersection_surface

        i_j_intersection = [' –> '.join(i_to_intersection_surface),
                            ' -> '.join(j_to_intersection_surface),
                            ''.join(m.surface for m in filter(lambda x: x.pos != '記号', sentence[intersection].morphs))]
        return ' | '.join(i_j_intersection)


def noun_to_noun(sentence):
    noun_idx = [i for i, c in
                 filter(lambda i_chunk: i_chunk[1].filter_for_morph(lambda x: x.pos == '名詞'), enumerate(sentence))]
    if len(noun_idx) < 2:
        return None
    else:
        for i in noun_idx:
            tmp = noun_idx[noun_idx.index(i):]
            tmp.remove(i)
            for j in tmp:
                print(i_to_j(sentence, i, j))
            return None

if __name__ == '__main__':
    document = load_neko_chunk()
    for idx in 8, 9, 10:
        print(idx)
        noun_to_noun(document[idx])
