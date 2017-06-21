# -*- coding: utf-8 -*-
import xml.etree.ElementTree as et


def mention_parse(mention):
    sentence = int(mention.find('./sentence').text)-1
    start = int(mention.find('./start').text)-1
    end = int(mention.find('./end').text)-1
    if start == end:
        print(sentence, start, end)
    return sentence, start, end


def get_document_from_xml(root):
    sentences = sorted(root.findall('.//sentences/sentence'), key=lambda x: int(x.attrib['id']))
    document = [[w.find('./word').text for w in sorted(sentence.findall('./tokens/token'), key=lambda x: int(x.attrib['id']))]
                for sentence in sentences]
    return document


def coreference(path='../../data/nlp.txt.xml'):
    root = et.parse(path).getroot()
    document = get_document_from_xml(root)
    coreferences = root.findall('.//coreference/coreference')

    men_rep = []  # [((sentence_idx, start, end), replace_word) ...]

    for coref in coreferences:
        # mentionを用意
        mentions = coref.findall('./mention')
        representative_mention = None
        other_mentions = []
        for m in mentions:
            if 'representative' in m.attrib.keys() and m.attrib['representative'] == 'true':
                representative_mention = m
            else:
                other_mentions.append(m)

        # mentionから置換文字列と,非置換文字列(場所)を生成
        if representative_mention and other_mentions:
            sentence_idx, start, end = mention_parse(representative_mention)
            replace_word = '[%s]' % (' '.join(document[sentence_idx][start:end]))
            # replace_idxes = set(mention_parse(m) for m in other_mentions)
            men_rep += [(mention_parse(m), replace_word) for m in other_mentions]
        else:
            pass

    # men_repのstart-end幅が狭いものから順に置換
    for m_r in sorted(men_rep, key=lambda mr: mr[0][2]-mr[0][2]):
        m, r = m_r
        replaced = '_(%s)_' % ' '.join(filter(lambda x: x != '', document[m[0]][m[1]:m[2]]))
        document[m[0]][m[1]] = r+replaced
        document[m[0]][m[1]+1:m[2]] = ['' for _ in range(m[2]-m[1]-1)]

    return document

if __name__ == '__main__':
    s = '\n\n'.join(' '.join(w for w in filter(lambda x: x != '', sentence)) for sentence in coreference())
    s = s.replace(' .', '.').replace(' ,', ',')
    print(s)
