import re

s = '13Nura73lksadflL;l;;..ashdkfauwe-980124zhlkfbcv'
pattern = r'.{5}'
print(re.findall(pattern, s))

# * - [0; \infty)
# + - [1; \infty)
# ? - [0; 1]
