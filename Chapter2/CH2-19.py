# coding:utf-8
# cut -f 1 popular-names.txt | sort | uniq -c | sort -r
import pandas as pd

path = './popular-names.txt'
df = pd.read_csv(path, sep='\t', header=None)
df.columns = ['Name', 'Sex', 'Count', 'Year']

print(df['Name'].value_counts())
