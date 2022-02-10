# difference 
# Hint : in 
def difference(arr1, arr2):
    ans = []
    for number in arr1:
        if number not in arr2:
            ans.append(number)
    return ans

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(*difference(arr1, arr2))