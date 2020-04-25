# coding:utf-8

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
word = s.split()
keys = []
values = []
n = len(word)

for i in range(n):
    tmp = word[i]

    if i == 0 or 4 <= i <= 8 or i == 14 or i == 15 or i == 18:
        keys.append(tmp[0])
        values.append(i + 1)
    else:
        keys.append(tmp[0:2])
        values.append(i + 1)

ans = dict(zip(keys, values))
print(ans)
