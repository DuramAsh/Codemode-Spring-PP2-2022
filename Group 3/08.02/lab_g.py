n = int(input())
d = dict()
for i in range(n):
    name, weak = input().split()
    d[name] = weak
m = int(input())
hunters = dict()
for i in range(m):
    temp = []
    name, weak, amount = map(str, input().split())
    if hunters.get(weak, 0) == 0:
        hunters[weak] = int(amount)
    else:
        hunters[weak] += int(amount)
cnt = 0
