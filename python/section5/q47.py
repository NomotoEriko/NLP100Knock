# -*- coding: utf-8 -*-
from q41 import load_neko_chunk
from pprint import pprint


def kinoudoushikoubun_sentence(sentence):
    result = {}
    for i, chunk in enumerate(sentence):
        i_m = [(i, m.surface) for i, m in filter(lambda im: im[1].pos1 == 'サ変接続', enumerate(chunk.morphs))]
        s_idx = set([i[0] for i in i_m])
        wo_idx = set([i-1 for i, m in filter(lambda im: im[1].base == 'を', enumerate(chunk.morphs))])
        s_wo = s_idx & wo_idx
        if len(s_wo) == 0:
            pass
        else:
            v = ''.join(m+'を' for i, m in i_m)
            suru = sentence[chunk.dst]
            srcs = suru.srcs
            srcs.remove(i)
            suru = [s.base for s in filter(lambda x: '動詞' in x.pos, suru.morphs)]
            if len(suru) == 0:
                pass
            else:
                v += suru[0]
            for src in srcs:
                src_surface = ''.join(s.surface for s in filter(lambda x: x.pos != '記号', sentence[src].morphs))
                kaku_kou = set((z.base, src_surface) for z in filter(lambda x: x.pos == '助詞', sentence[src].morphs))
                if v in result.keys():
                    result[v].update(kaku_kou)
                else:
                    result[v] = set(kaku_kou)
    return result


def kinoudoushikoubun_document(document):
    result_document = {}
    for sentence in document:
        result_sentence = kinoudoushikoubun_sentence(sentence)
        for k, v in result_sentence.items():
            if k in result_document.keys():
                result_document[k].update(v)
            else:
                result_document[k] = v
    return result_document


def print_kinoudoushi(kinoudoushi):
    for k, v in kinoudoushi.items():
        v = sorted(v, key=lambda x: x[0])
        print('%s\t%s\t%s' % (k, ' '.join(x[0] for x in v), ' '.join(x[1] for x in v)))


if __name__ == '__main__':
    print_kinoudoushi(kinoudoushikoubun_document(load_neko_chunk()))