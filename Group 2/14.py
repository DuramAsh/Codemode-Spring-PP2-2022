s = "Hello, CODEMODE!"
# start_index = 0
# end_index = len(s)
# step = 1
n = int(input())
s1 = s[ : n] # [0, n)
s2 = s[n : ] # [n, len(s))
s3 = s[n : : -1] # [n, n + n) step = -1
print(s1)
print(s2)
print(s3)