arr = list(map(int, input().split()))
position = len(arr) - 1

for i in range(len(arr) - 2, -1, -1):
    if i + arr[i] >= position:
        position = i

if position == 0:
    print(1)
else:
    print(0)