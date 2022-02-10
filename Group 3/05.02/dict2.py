d = dict()
n = int(input())
for i in range(n):
    name, money = map(str, input().split())
    #1
    if name not in d.keys():
        d[name] = int(money)
    else:
        d[name] += int(money)
        # d[name] = d[name] + int(money)
    #2
    # if d.get(name, 0) == 0:
    #     d[name] = int(money)
    # else:
    #     d[name] += int(money)
    #3
    # d[name] = d.get(name, 0) + int(money)
# d[name] = 0
print(d)