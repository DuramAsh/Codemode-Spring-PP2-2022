arr = list(map(int, input().split()))
cnt = 0
for number in arr:
    if number != 0:
        print(number, end=' ')
    else:
        cnt += 1
print('0 ' * cnt)