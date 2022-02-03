arr = list(set(i) for i in input().split())
# strings = input().split()
# arr1 = []
# for i in strings:
#     arr1.append(set(i))
# print(arr)
s = arr[0]
for i in arr:
    s = s.intersection(i)
    # print(*s, sep='')
print(*sorted(s), sep='')