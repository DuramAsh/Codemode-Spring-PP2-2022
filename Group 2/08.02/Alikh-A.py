arr = list(map(int, input().split()))
pos = len(arr) - 1
for i in range(len(arr) - 2, -1, -1):
    if arr[i] + i >= pos:
        pos = i
    print(pos, end='; ')
print()
print(f'After for : {pos}')
if pos == 0:
    print(1)
else:
    print(0)