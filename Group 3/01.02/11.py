#1 2 3 4 5
#1 2
#2 3
#3 4
#4 5
l1 = list(map(int, input().split()))
for i in range(len(l1) - 1):
    print(l1[i], l1[i + 1])