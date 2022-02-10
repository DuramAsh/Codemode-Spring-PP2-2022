arr = list(map(int, input().split()))
position = len(arr) - 1

for i in range(len(arr) - 2, -1, -1):
    if i + arr[i] >= position:
        position = i
    # print(f'going_to:{position};ind={i}', end=' <- \n')
# print()
if position == 0:
    print(1)
else:
    print(0)