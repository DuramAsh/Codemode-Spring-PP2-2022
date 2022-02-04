words = list(map(str, input().split()))
arr = [set(word) for word in words]
print(arr)
s = arr[0]
for i in arr:
    # print(s, i, sep='-->')
    s = s.intersection(i)
