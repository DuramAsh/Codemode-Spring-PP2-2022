def rec_print(s, i = 0):
    
    if len(s) == i:
        return

    print(s[i], end='')

    rec_print(s, i + 1)


s = input()
rec_print(s)