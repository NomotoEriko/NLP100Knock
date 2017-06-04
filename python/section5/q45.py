# -*- coding: utf-8 -*-
from q41 import load_neko_chunk
from pprint import pprint

def kaku_pattern_sentence(sentence):
    result = {}
    verbe = []
    for c in filter(lambda x: x.filter_for_morph(lambda x: x.pos == '動詞'), sentence):
        verbe.append(c)
    for chunk in verbe:
        v = [s for s in filter(lambda x:x.pos == '動詞', chunk.morphs)]
        v = v[0].base
        for src in chunk.srcs:
            if v in result.keys():
                result[v].update(set(z.base for z in filter(lambda x: x.pos == '助詞', sentence[src].morphs)))
            else:
                result[v] = set(z.base for z in filter(lambda x: x.pos == '助詞', sentence[src].morphs))
    return result


def kaku_pattern_document(document):
    document_result = {}
    for sentence in document:
        sentence_result = kaku_pattern_sentence(sentence)
        for key in sentence_result.keys():
            if key in document_result.keys():
                document_result[key].update(sentence_result[key])
            else:
                document_result[key] = sentence_result[key]
    return document_result


def print_kaku(kaku_pattern):
    if type(kaku_pattern) == dict:
        for k, v in kaku_pattern.items():
            print('%s\t%s' % (k, ' '.join(sorted(v))))
    elif type(kaku_pattern) == list:
        for k, v in kaku_pattern:
            print('%s\t%s' % (k, ' '.join(sorted(v))))


if __name__ == '__main__':
    print_kaku([(k, kaku_pattern_document(load_neko_chunk())[k]) for k in ('する', '見る', '与える')])

