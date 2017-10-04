# -*- coding: utf-8 -*-
data_path = "../../data/enwiki-20150112-400-r100-10576.txt"


def load_txt(data=data_path):
    return [line for line in open(data, 'r')]


def shaping(lines, save_name="q80.txt"):
    result = []
    for line in lines:
        words = line.split(' ')
        words = [word.strip().strip(".,!?;:()[]'\"") for word in words]
        line = ' '.join(word for word in words if word)
        result.append(line)
    with open(save_name, 'w') as f:
        f.write('\n'.join(result))

if __name__ == '__main__':
    shaping(load_txt())
