from random import shuffle


def typo(string=None):
    if None == string:
        print('E: Empty string')
        return None
    else:
        words = []
        for s in string.split(' '):
            if len(s) > 3:
                s_inner = list(s[1:-1])
                shuffle(s_inner)
                words.append(s[0]+''.join(s_inner)+s[-1])
            else:
                words.append(s)
        return ' '.join(words)


if __name__ == '__main__':
    string = "I couldn't believe that I could actually understand what I was reading :" \
             " the phenomenal power of the human mind ."
    print(typo(string))
