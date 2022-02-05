# sum(list)
# print(sum([1,2,3]))
# slicing
arr = list(map(int, input().split()))
for i in range(len(arr)):
    # print(arr[:i],arr[i + 1:], sep= ' - ')
    if sum(arr[ :i ]) == sum(arr[ i+1:]):
        print(i)
        exit() # return 0
print(-1)
