from q30 import load_neko
import pandas as pd
from pprint import pprint
neko = load_neko()
nouns = set()

for sentence in neko:
    morphos = pd.DataFrame(sentence)
    nouns.update(
        morphos[(morphos['pos1'] == 'サ変接続') & (morphos['pos'] == '名詞')]['base'].tolist()
    )

pprint(nouns)
