arr = list(map(int, input().split()))
# print(*arr)
for i in range(len(arr)):
    if sum(arr[:i]) == sum(arr[i + 1:]):
        print(i)
        exit()
print(-1)