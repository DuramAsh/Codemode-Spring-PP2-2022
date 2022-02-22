import re

with open('raw.data', 'r', encoding='utf8') as f:
    x = f.read()
    

pattern = r''
y = re.search(pattern, x)
print(y.group('bin'))
print(y.group('check'))

# 1. Вытащить бин и его номер
# 2. Вытащить номер Чека