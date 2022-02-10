def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]

s = 'Leetcode'
x = rev_str(s)

for i in range(len(s)):
    print(next(x), end='')