# coding:utf-8
# cat popular-names.txt  | tr '\t' ' ' > out.txt
# expand -t 1 popular-names.txt > out.txt

path = './popular-names.txt'

with open(path) as f:
    for line in f:
        print(line.replace('\t', ' '), end='')
