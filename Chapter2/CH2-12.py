# coding:utf-8
import pandas as pd
# cut -f 1 popular-names.txt
# cut -f 2 popular-names.txt
# cutコマンドはデフォルトでタブがデリミタになっている

path = './popular-names.txt'

df = pd.read_csv(path, sep='\t', header=None)
df.columns = ['Name', 'Sex', 'Count', 'Year']
print(df)


col1 = df['Name']
col2 = df['Sex']

col1.to_csv('./col1.txt', header=None, index=None)
col2.to_csv('./col2.txt', header=None, index=None)
