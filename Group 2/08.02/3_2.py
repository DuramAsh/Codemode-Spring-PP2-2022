arr = list(map(int, input().split()))
for number in arr:
    if number == 0:
        arr.remove(0)
        arr.append(0)
print(*arr)