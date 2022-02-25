import re
n = int(input())
for _ in range(n):
    pattern = r'[+-]?[0-9]*\.[0-9]+$'
    print(bool(re.match(pattern, input())))