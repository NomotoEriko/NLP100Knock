import pickle
from collections import Counter
import pandas as pd
from matplotlib import pyplot as plt

with open('freq_all_words.pickle', 'rb') as f:
    words = pickle.load(f)

freq_hist = pd.Series(Counter(words.values()))
left = freq_hist.index.tolist()
height = freq_hist.values.tolist()
plt.bar(left=left, height=height, align='center')
plt.savefig('all_frequency_histgram')

plt.clf()
left = freq_hist[:100].index.tolist()
height = freq_hist[:100].values.tolist()
plt.bar(left=left, height=height)
plt.xlim([0, 100])
plt.savefig('top100_frequency_histgram')
