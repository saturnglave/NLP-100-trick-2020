# coding:utf-8
import pandas as pd

df = pd.read_csv('./popular-names.txt', sep='\t', header=None)
print(df)


print(len(df))
