import re
print(sum([int(price.replace(' ', '')) for price in re.findall(r'Стоимость\n([\d\s]+)', open('raw.data','r', encoding='utf-8').read())]))