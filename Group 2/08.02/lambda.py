arr = list(map(int, input().split()))
def our_sort(x, y):
    return (y > x) - (y < x)
print(*sorted(arr, key=lambda x, y : (y > x) - (y < x)))

