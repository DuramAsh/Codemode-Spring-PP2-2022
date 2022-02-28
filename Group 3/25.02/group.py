import re
pattern = r'([a-zA-Z0-9])\1+'
ans = re.search(pattern, input())
if ans:
    print(ans.group(1))
    #111 - group(0)
    #1 - group(1)
else:
    print(-1)