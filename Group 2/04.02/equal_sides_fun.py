from re import I


def find_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1

print(find_index(list(map(int, input().split()))))