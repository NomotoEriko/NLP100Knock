def load_neko():
    neko = []
    sentence = []
    for line in open('../../data/neko.txt.mecab', 'r'):
        if line[:3] != 'EOS':
            surface, elems = line.split('\t')
            elems = elems.split(',')
            morpheme = {
                'surface': surface, 'base': elems[6], 'pos': elems[0].strip(), 'pos1': elems[1].strip()
            }
            sentence.append(morpheme)
        else:
            if len(sentence) != 0:
                neko.append(sentence)
            sentence = []
    return neko

if __name__ == '__main__':
    neko = load_neko()
    from pprint import pprint
    pprint(neko[:2])
