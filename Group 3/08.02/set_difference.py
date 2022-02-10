l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(*set(l1).difference(set(l2)))