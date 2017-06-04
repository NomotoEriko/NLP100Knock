# -*- coding: utf-8 -*-
from q41 import load_neko_chunk
from pprint import pprint


def kaku_pattern_kou_sentence(sentence):
    result = {}
    verbe = []
    for c in filter(lambda x: x.filter_for_morph(lambda x: x.pos == '動詞'), sentence):
        verbe.append(c)
    for chunk in verbe:
        v = [s for s in filter(lambda x:x.pos == '動詞', chunk.morphs)]
        v = v[0].base
        for src in chunk.srcs:
            kaku_kou = set((z.base, ''.join(s.surface for s in filter(lambda x: x.pos != '記号', sentence[src].morphs)))
                           for z in filter(lambda x: x.pos == '助詞', sentence[src].morphs))
            if v in result.keys():
                result[v].update(kaku_kou)
            else:
                result[v] = set(kaku_kou)
    return result


def kaku_pattern_kou_document(document):
    document_result = {}
    for sentence in document:
        sentence_result = kaku_pattern_kou_sentence(sentence)
        for k, v in sentence_result.items():
            if k in document_result.keys():
                document_result[k].update(v)
            else:
                document_result[k] = v
    return document_result


def print_kaku_kou(kaku_kou_pattern):
    for k, v in kaku_kou_pattern.items():
        v = sorted(v, key=lambda x: x[0])
        print('%s\t%s\t%s' % (k, ' '.join(x[0] for x in v), ' '.join(x[1] for x in v)))

if __name__ == '__main__':
    print_kaku_kou(kaku_pattern_kou_document(load_neko_chunk()))
