arr = list(map(int, input().split()))
for i in range(len(arr)):
    # print(arr[:i], arr[i + 1:])
    if sum(arr[:i]) == sum(arr[i + 1:]):
        print(i)
        exit() # aka. return 0;
print(-1)