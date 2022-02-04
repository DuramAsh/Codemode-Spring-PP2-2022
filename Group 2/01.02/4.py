l1 = [int(i) for i in input().split()]
# for i in l1:
#     print(i, end=' ')
for i in range(len(l1) - 1):
    print(l1[i], l1[i + 1], sep=' + ')