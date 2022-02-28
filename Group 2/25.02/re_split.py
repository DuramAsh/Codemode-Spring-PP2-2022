import re
pattern = r'[0-9]+'
s = 'Nura1123123123Zhaks2Adil3Bauka4'
l = re.split(pattern, s)
print(*l)