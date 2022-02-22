import re

s = 'abcabcfhJ123Igokababddab'
pattern = r'[aeiuoAEIUO]' # raw

x = re.search(pattern, s)
y = re.match(pattern, s)
z = re.findall(pattern, s)
w = re.finditer(pattern, s)
# print(x, y, sep='\n')
print(z)

# for i in w:
    # print(i.span())
    # print(i.start())
    # print(i.end())