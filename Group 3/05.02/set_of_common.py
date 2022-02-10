words = input().split()
arr = []
for word in words:
    arr.append(set(word))
s = arr[0]
for i in range(1,len(arr)):
    # print(s,arr[i],sep='<-->')
    s.intersection_update(arr[i])

print(*sorted(s), sep='')