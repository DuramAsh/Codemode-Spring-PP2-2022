import re

text = '13Nura73lksadflL;l;5;..ashdkfauwe-9 80124zhlkfbcv'
pattern = r'\w{8,}\s'

ls = re.findall(pattern, text)
print(ls)