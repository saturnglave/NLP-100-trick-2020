# coding:utf-8
import pandas as pd
import re
import requests


def uk_load():
    path = './jawiki-country.json.gz'
    wiki = pd.read_json(path, compression='infer', orient='records', lines=True)
    uk = wiki[wiki['title'] == 'イギリス']['text'].values[0]
    return(uk)


def main():
    uk_txt = uk_load()
    uk_basic = re.findall(r'\|(.+?) \= (.+)', uk_txt)
    uk_dict = {}

    for item in uk_basic:
        tmp = re.sub(r'\{\{(.+)\|\[\[ファイル:(.+)\]\]\}\}', r'\2', item[1])
        tmp = re.sub(r'\[\[(?:ファイル|File):(.+?)\|(.+?)\]\]', r'\1', tmp)
        tmp = re.sub(r'\{\{lang\|(?:en|fr)\|(.+)\}\}', r'\1', tmp)
        tmp = re.sub(r'\{\{仮リンク\|(.+)\|(.+)\|(.+)\}\}', r'\1 \3', tmp)
        tmp = tmp.replace('{{en icon}}', '').replace('{{center|[[ファイル：', '')
        tmp = tmp.replace('[[', '').replace(']]', '').replace('{{', '').replace('}}', '')
        tmp = re.sub(r'\|', ' ', tmp)
        tmp = re.sub(r'<(.+?)>$', '', tmp)
        tmp = re.sub(r'<br \/>', ' ', tmp)
        tmp = tmp.replace('\'\'\'', '').replace('\'\'', '').replace(':en:', '')
        uk_dict[item[0]] = tmp

    # print(uk_dict)
    # print(uk_dict['国旗画像'])

    url = 'https://www.mediawiki.org/w/api.php'
    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": 'File:' + uk_dict['国旗画像'],
        "iiprop": "url"
    }

    r = requests.get(url, params=params)
    result = r.json()
    # print(result)

    df = pd.json_normalize(result)
    url = df['query.pages.-1.imageinfo'].values[0]
    # print(url)
    print(url[0]['url'])


if __name__ == "__main__":
    main()
