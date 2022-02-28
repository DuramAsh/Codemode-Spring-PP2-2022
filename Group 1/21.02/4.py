import re

with open('raw.data', 'r', encoding='utf8') as f:
    x = f.read()

pattern = r'БИН\s(?P<bin>\d+)'
pattern2 = r'Серия\s(?P<series>\d+)'


print(re.search(pattern, x).group("bin"))
print(re.search(pattern2, x).group("series"))
