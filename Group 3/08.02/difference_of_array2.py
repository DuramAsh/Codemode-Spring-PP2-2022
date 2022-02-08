def difference(arr1, arr2):
    return [number for number in arr1 if number not in arr2]

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(*difference(arr1, arr2))