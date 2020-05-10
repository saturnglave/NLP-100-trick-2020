# coding:utf-8
import pandas as pd
import re

# 結果的に25-28の内容全部一気にやった


def uk_load():
    path = './jawiki-country.json.gz'
    wiki = pd.read_json(path, compression='infer', orient='records', lines=True)
    uk = wiki[wiki['title'] == 'イギリス']['text'].values[0]
    return(uk)


def main():
    uk_txt = uk_load()
    uk_basic = re.findall(r'\|(.+?) \= (.+)', uk_txt)
    ans = {}

    '''
    for item in uk_basic:
        print(item)
    print('')
    '''

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
        ans[item[0]] = tmp

    print(ans)


if __name__ == "__main__":
    main()
