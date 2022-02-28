import re
# \n - newline in pattern

with open('raw.data', 'r', encoding='utf8') as f:
    x = f.read()
    
# print(x)
pattern = r'Стоимость\n(?P<Price>[\d\s]+)'
# pattern = r'Стоимость\n(?P<Price>[\d\s]+,\d{2})'

arr = re.findall(pattern, x)
# print(len(arr), arr)
modified_arr = [int(i.replace(' ', '')) for i in arr]
print(modified_arr)
print(sum(modified_arr))