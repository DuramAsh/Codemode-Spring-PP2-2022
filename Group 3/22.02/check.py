import re
with open('raw.data','r', encoding='utf-8') as f:
    text = f.read()
#patternBin = r'БИН (\d{12})'
#print(re.search(patternBin,text).group(1))
# pattern = r'Стоимость\n([0-9]{1,3} [0-9]{3}|[0-9]{1,3})'
pattern = r'Стоимость\n([\d\s]+)'
pattern_2 = r'[0-9]+\.\n()+\n$'
#1 152
#152
prices = re.findall(pattern, text)
# print(prices, len(prices))
prices = [int(price.replace(' ', '')) for price in prices]
print(sum(prices))