# coding:utf-8

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
word = s.split()
ans = []

for item in word:
    ans.append(len(item) - item.count(',') - item.count('.'))

print(ans)
