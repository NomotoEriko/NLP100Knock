from q30 import load_neko
import pandas as pd
from pprint import pprint

neko = load_neko()
noun_noun = set()
for sentence in neko:
    morphs = pd.DataFrame(sentence)
    noun_idx = morphs[morphs['pos'] == '名詞'].index.tolist()
    word = ''
    for idx in noun_idx:
        word += morphs['surface'][idx]
        if idx+1 not in noun_idx:
            noun_noun.add(word)
            word = ''

pprint(noun_noun)
