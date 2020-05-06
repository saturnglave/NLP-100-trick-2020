# coding:utf-8
import pandas as pd
import re


def uk_load():
    path = './jawiki-country.json.gz'
    wiki = pd.read_json(path, compression='infer', orient='records', lines=True)
    uk = wiki[wiki['title'] == 'イギリス']['text'].values[0]
    return(uk)


def main():
    uk_txt = uk_load()
    file = re.findall(r'\[\[(?:ファイル|File):(.+?)\|(.+?)\]\]', uk_txt)

    for item in file:
        print(item[0])


if __name__ == "__main__":
    main()
