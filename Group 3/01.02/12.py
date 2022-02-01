#1
l1 = list(map(int, input().split()))
#2
l1 = [int(i) ** 2 for i in input().split()]
#2.1
# l1 = []
# for i in input().split():
#     l1.append(i)
print(*l1)