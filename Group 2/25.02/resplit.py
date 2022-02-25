import re
s = input()
pattern = r'[.,]'
list = list(re.split(pattern, s))
print(*list, sep='\n')