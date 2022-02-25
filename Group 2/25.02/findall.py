import re
pattern = r'([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])(?P<vowels>[aeiouAEIOU]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]'

s = input()
arr = re.findall(pattern, s, re.I)
if not arr:
    print(-1)
    exit()
print(*arr, sep='\n')

matches = re.finditer(r'(?=(\d{10}))',s)
results = [int(match.group(1)) for match in matches]