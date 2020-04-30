# coding:utf-8
# wc -l popular-names.txt → 2780 popular-names.txt

path = './popular-names.txt'
ans = 0

with open(path) as f:
    for line in f:
        ans += 1

print(ans)
