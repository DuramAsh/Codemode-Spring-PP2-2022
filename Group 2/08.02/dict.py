d = dict()
n = int(input())

def sort_dict(p1, p2):
    return p1[1] < p2[1]

for i in range(n):
    name, money = input().split()
    d[name] = int(money)
for name, money in sorted(d, key=sort_dict()):
    print(name, money)