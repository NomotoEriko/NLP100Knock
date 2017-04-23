import pickle
import pandas as pd
from matplotlib import pyplot as plt
with open('freq_all_words.pickle', 'rb') as f:
    freq = pd.Series(sorted(pickle.load(f).values(), key=lambda x: -x))

plt.yscale('log')
plt.xscale('log')
plt.plot(freq.index.tolist(), freq.values.tolist())
plt.savefig('log-log')
