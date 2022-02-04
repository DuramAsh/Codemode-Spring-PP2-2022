words = list(map(str, input().split()))
arr = [set(word) for word in words]
# arr = []
# for word in words:
#     arr.append(set(word))


print(arr)
s = arr[0]
for elem in arr:
    # print(s, i, sep='-->')
    print(elem, type(elem))
    # s = s.intersection(elem)
print(*sorted(set(s)), sep='')