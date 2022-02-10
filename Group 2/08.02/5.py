n = 5
arr = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# arr = [[0] * n] * n
print(arr)

for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j] = i * j
        elif i == 0:
            arr[i][j] = j
        elif j == 0:
            arr[i][j] = i

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()