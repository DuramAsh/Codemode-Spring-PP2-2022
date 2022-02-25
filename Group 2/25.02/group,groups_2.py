import re
pattern = r'([a-zA-Z0-9])\1+'
s = input()
l = re.findall(pattern, s)
# print(*l)
if l:
    print(l[0])
else:
    print(-1)