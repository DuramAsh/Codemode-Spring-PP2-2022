arr = list(map(int,input().split()))
dp = [0 for _ in range(len(arr))]
for i in range(len(arr)):
    if i == 0:
        dp[i + arr[i]] += 1
    elif i + arr[i] < len(arr) and dp[i] == 1:
        dp[i + arr[i]] += 1
if dp[len(arr) - 1] == 0:
    print(0)
else:
    print(1)