from matplotlib import pyplot as plt
import pickle
with open('freq_top50_words.pickle', 'rb') as f:
    words_top10 = pickle.load(f)[:10]

left = [i for i in range(1, 11)]
label = [w[0] for w in words_top10]
height = [w[1] for w in words_top10]
plt.bar(left=left, height=height, tick_label=label, align="center")
plt.savefig('top10_word_freq')
