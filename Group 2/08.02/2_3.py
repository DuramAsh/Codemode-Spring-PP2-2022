def difference(arr1, arr2):
    return [first for first in arr1 if first not in arr2]

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(*difference(arr1, arr2))