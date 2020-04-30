# coding:utf-8
# paste col1.txt col2.txt
import pandas as pd

p1 = './col1.txt'
p2 = './col2.txt'

df1 = pd.read_csv(p1, sep='\t', header=None)
df2 = pd.read_csv(p2, sep='\t', header=None)

df = pd.concat([df1, df2], axis=1)

df.to_csv('merge.txt', sep='\t', header=None)
