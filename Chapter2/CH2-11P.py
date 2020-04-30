# coding:utf-8
import pandas as pd

path = './popular-names.txt'

df = pd.read_csv(path, sep='\t', header=None)

print(df)

df.to_csv('./out.txt', sep=' ', header=None, index=None)
