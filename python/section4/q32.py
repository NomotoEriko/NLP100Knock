from q30 import load_neko
import pandas as pd
from pprint import pprint

neko = load_neko()
varbs = set()
for sentence in neko:
    morphos = pd.DataFrame(sentence)
    varbs.update(
        morphos[morphos['pos'] == '動詞']['base'].tolist()
    )
pprint(varbs)
