n = int(input())
d = {}
demons = []
for _ in range(n):
    name, weak = input().split()
    d[weak] = d.get(weak, 0) + 1
    # if weak not in d.keys():
    #     d[weak] = 1
    # else:
    #     d[weak] += 1

n = int(input())
for _ in range(n):
    name, weak, amount = input().split()
    if weak in d.keys():
        d[weak] -= amount
print(f'Demons left: {sum([i for i in d.value() if i > 0])}')