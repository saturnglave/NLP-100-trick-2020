# coding:utf-8
import pandas as pd

path = './popular-names.txt'
df = pd.read_csv(path, sep='\t', header=None)
df.columns = ['Name', 'Sex', 'Count', 'Year']

letter = set(df['Name'].str[0])
print(letter)
