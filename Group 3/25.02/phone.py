import re
n = int(input())
for _ in range(n):
    pattern = r'[789][0-9]{9}$'
    res = re.match(pattern, input())
    if res:
        print('YES')
    else:
        print("NO")

# codemode
# pattern = 'em'
# search = True code_EM_ode
# match = False CO != EM