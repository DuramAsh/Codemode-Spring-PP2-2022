d = {'ONE':'1',
'TWO':'2',
'THR':'3',
'FOU':'4',
'FIV':'5',
'SIX':'6',
'SEV':'7',
'EIG':'8',
'NIN':'9',
'ZER':'0'}
s = input()
ans = ''
for i in range(len(s)):
    if s[i:i + 3] in d.keys():
        ans += d[s[i:i + 3]]
    elif s[i] == '+':
        ans += '+'
# print(ans)
res = str(sum(list(map(int, ans.split('+')))))
# print(res)
reverse_dict = {k:v for v,k in d.items()}
print(''.join(reverse_dict[i] for i in res))