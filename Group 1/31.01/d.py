# Input:
# 5 9 13 52
# 3

# div = int(input())

# Output:
# 8 27 56 901
# Formula : (l[i] ^ 2) / 3

l = list(map(int, input().split()))
div = int(input())
for i in l:
    print(i ** 2 // div, end=' ')