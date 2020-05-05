# coding:utf-8
import pandas as pd
import re


def uk_load():
    path = './jawiki-country.json.gz'
    wiki = pd.read_json(path, compression='infer', orient='records', lines=True)
    uk = wiki[wiki['title'] == 'イギリス']['text'].values[0]
    return(uk)


def main():
    uk_txt = uk_load().split('\n')
    uk_category = list(filter(lambda x: "[[Category:" in x, uk_txt))
    # print(uk_category)
    for item in uk_category:
        item = item.replace('[[Category:', '').replace(']]', '')
        item = re.sub(r'\|.$', '', item)
        print(item)


if __name__ == "__main__":
    main()
