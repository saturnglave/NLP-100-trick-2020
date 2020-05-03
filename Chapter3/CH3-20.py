# coding:utf-8
import pandas as pd

path = './jawiki-country.json.gz'

df = pd.read_json(path, compression='infer', orient='records', lines=True)
# print(df)

ans = df.query('title == "イギリス"')['text'].values[0]


print(ans)
