def recursion(s, i = 0):
    if i == len(s):
        return
    print(s[i],end='')
    recursion(s, i + 1)
    
s = input()
recursion(s)