# coding:utf-8
import pandas as pd


def uk_load():
    path = './jawiki-country.json.gz'
    wiki = pd.read_json(path, compression='infer', orient='records', lines=True)
    uk = wiki[wiki['title'] == 'イギリス']['text'].values[0]
    return(uk)


def main():
    uk_txt = uk_load().split('\n')
    section = list(filter(lambda x: '==' in x, uk_txt))
    # print(section)

    for item in section:
        if item[:5] == '=====':
            print(item.replace('=====', '').replace(' ', ''), 4)
        elif item[:4] == '====':
            print(item.replace('====', '').replace(' ', ''), 3)
        elif item[:3] == '===':
            print(item.replace('===', '').replace(' ', ''), 2)
        elif item[:2] == '==':
            print(item.replace('==', '').replace(' ', ''), 1)


if __name__ == "__main__":
    main()
