import re


with open('t7.txt', 'r') as f:
    x = f.read()
    
patric = r'def\s(\w+)'
patterns = re.findall(patric, x)

print(*patterns, sep='\n')

