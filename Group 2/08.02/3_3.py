arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i] == 0:
        arr.pop(i)
        arr.append(0)
print(*arr)