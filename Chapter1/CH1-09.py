# coding:utf-8
import random

s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
ans = ''

for item in s.split():
    if len(item) <= 4:
        ans += item
    else:
        tmp = ''.join(random.sample(item[1:-1], len(item) - 2))
        ans += item[0] + tmp + item[-1]
    ans += ' '

print(ans)
