from q30 import load_neko
import pandas as pd
from pprint import pprint

neko = load_neko()
noun_no_noun = set()
for sentence in neko:
    morphs = pd.DataFrame(sentence)
    noun_idx = morphs[morphs['pos'] == '名詞'].index.tolist()
    no_idx = morphs[morphs['surface'] == 'の'].index.tolist()

    for idx in noun_idx:
        if idx+1 in no_idx and idx+2 in noun_idx:
            noun_no_noun.add(''.join(morphs.ix[[idx, idx+1, idx+2], :]['surface'].tolist()))


pprint(noun_no_noun)
