from collections import Counter
from q30 import load_neko
import pandas as pd
from pprint import pprint
import pickle

def get_freqency():
    neko = load_neko()
    counter_words = Counter([])
    for sentence in neko:
        morphs = pd.DataFrame(sentence)
        counter_words = counter_words + Counter(morphs['base'].tolist())
    return counter_words

if __name__ == '__main__':
    freq = get_freqency()
    pprint(freq.most_common(50))
    with open('freq_top50_words.pickle', 'wb') as f:
        pickle.dump(freq.most_common(50), f)
    with open('freq_all_words.pickle', 'wb') as f:
        pickle.dump(freq, f)
