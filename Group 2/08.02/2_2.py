def difference(arr1, arr2):
    ans = []
    for first in arr1:
        if first not in arr2:
            ans.append(first)
    return ans

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(*difference(arr1, arr2))