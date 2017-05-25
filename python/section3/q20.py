# -*- coding: utf-8 -*-
import json
from pprint import pprint
import pandas as pd
import os


def load_json():
    data_path = '../../data/jawiki-country.json'
    json_data = []
    for line in  open(data_path, 'r'):
        json_data.append(json.loads(line))
    return json_data


def load_json_pandas():
    return pd.DataFrame(load_json())


def picup_eng_txt():
    data = load_json_pandas()
    return data.loc[data.title == 'イギリス', 'text'].values[0]


if __name__ == '__main__':
    eng_txt = picup_eng_txt()
    print(eng_txt)
