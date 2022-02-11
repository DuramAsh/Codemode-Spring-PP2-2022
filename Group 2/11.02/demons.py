n = int(input())
d = {}
demons = []
for _ in range(n):
    name, weak = input().split()
    d[weak] = d.get(weak, 0) + 1
    # print(*d.items(), end='\n')
    # if weak not in d.keys():
    #     d[weak] = 1
    # else:
    #     d[weak] += 1

n = int(input())
for _ in range(n):
    name, weak, amount = input().split()
    if weak in d.keys():
        d[weak] -= int(amount)

demons_left = sum([i for i in d.values() if i > 0])
print(f'Demons left: {demons_left}')