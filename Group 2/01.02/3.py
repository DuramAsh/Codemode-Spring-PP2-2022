# for (int i = 0; i < 10; ++i) {
#     pass
# }

# for i in range(0, 10, 1):
#     print(i, end=' ')
# for i in range(10):
#     print(i)
# l1 = list(map(int, input().split()))
l2 = [int(i) for i in input().split()]
print(*l2)

