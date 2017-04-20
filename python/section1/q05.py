def make_ngram(n=2, sequence=None):
    if None == sequence:
        print('E: Empty sequence.')
        return None
    else:
        seqlist = []
        for i in range(n):
            seqlist.append(sequence[i:])
        ngram = [[seq[j] for seq in seqlist] for j in range(len(seqlist[-1]))]
        return ngram

if __name__=='__main__':
    string = "I am an NLPer"
    word_bi_gram = make_ngram(sequence=string.split(' '))
    char_bi_gram = make_ngram(sequence=string)
    print(word_bi_gram)
    print(char_bi_gram)
