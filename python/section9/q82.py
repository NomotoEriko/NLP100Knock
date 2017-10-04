# -*- coding: utf-8 -*-
from random import randint
from collections import deque
from q80 import load_txt


def main():
    save_file = "q82.txt"
    lines = load_txt("q81.txt")
    result = []
    for line in lines:
        words = line.strip().split(' ')
        words += [None] * 5
        window = deque([None for _ in range(6)], maxlen=11)
        window += words[:5]
        for word in words[5:]:
            window.append(word)
            if window[5] is not None:
                d = randint(1, 5)
                lwindow = list(window)
                c = lwindow[5-d:5] + lwindow[6:6+d]
                c = [x for x in c if x]
                if c:
                    result.append(lwindow[5] + "\t" + ','.join(c))
    with open(save_file, 'w') as f:
        f.write("\n".join(result))
    print("complete!")


if __name__ == '__main__':
    main()
