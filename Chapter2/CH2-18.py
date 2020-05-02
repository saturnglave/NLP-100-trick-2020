# coding:utf-8
import pandas as pd

path = './popular-names.txt'

df = pd.read_csv(path, sep='\t', header=None)
df.columns = ['Name', 'Sex', 'Count', 'Year']

df_s = df.sort_values('Year', ascending=False)
df_s.reset_index(inplace=True, drop=True)
print(df_s)
