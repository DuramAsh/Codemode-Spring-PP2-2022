# l1 = list(map(int, input().split('a')))
# # map(int, input().split())
# print(l1)
# # print(a, b, c)
















# input: 1 3 5 1 -10
# output: 2.0 4.0 3.0 -4.5

l1 = list(map(int, input().split()))
l2 = []
for i in range(len(l1) - 1):
    l2.append((l1[i] + l1[i + 1]) / 2)
print(*l2)