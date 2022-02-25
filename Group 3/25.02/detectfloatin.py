import re
pattern = r'[+-]?\d*\.\d+$'
n = int(input())
for _ in range(n):
    s = input()
    print(bool(re.match(pattern, s)))