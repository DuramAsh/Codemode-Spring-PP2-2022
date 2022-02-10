# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
# print(*set(arr1).difference(set(arr2)))

#set param
#1
#Only unique elements
#Unsorted, unindexed
arr1 = list(map(int, input().split()))
s = set(arr1)
print(*s)
#union, intersection, difference
