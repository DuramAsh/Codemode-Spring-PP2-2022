def recursion_print(s : str, i = 0):
    if len(s) == i:
        return 
    
    print(s[i], end='')
    
    recursion_print(s, i + 1)
    
s = input()
recursion_print(s)