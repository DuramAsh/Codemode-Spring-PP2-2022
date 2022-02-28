import re

with open('raw.data', 'r', encoding='utf8') as f:
    x = f.read()
    
pattern = r'БИН (?P<bin>[0-9]+)'
price_p = r'Стоимость\n(?P<price>[1-9]{1,3} [0-9]{3}|[0-9]{1,3})'
# y = re.search(pattern, x)
# print(y.group('bin'))
# print(y.group('check'))

prices = re.findall(price_p, x)
prices = [price.replace(' ','') for price in prices]
# print(*prices)
print(sum(list(map(int, prices))))

# 1. Вытащить бин и его номер
# 2. Вытащить номер Чека