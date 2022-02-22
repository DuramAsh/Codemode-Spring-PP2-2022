import re

with open('raw.data', 'r', encoding='utf-8') as f:
    x = f.read()
    
print(x)

# 1. Вытащить бин и его номер
# 2. Вытащить номер Чека