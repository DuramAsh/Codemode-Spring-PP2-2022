import re
pattern = r'([a-zA-Z0-9])\1+'
s = input() # ..12345678910111213141516171820212223
l = re.search(pattern, s)
if l:
    print(l.group(1))
else:
    print(-1)
