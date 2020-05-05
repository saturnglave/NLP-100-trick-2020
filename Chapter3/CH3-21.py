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
    ans = []
    # print(uk_txt)

    for item in uk_txt:
        result = re.search(r'^\[\[Category:.+\]\]$', item)
        if result:
            ans.append(result.group(0))

    for r in ans:
        print(r)


if __name__ == "__main__":
    main()
