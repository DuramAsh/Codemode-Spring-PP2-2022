def to_lower(s):
    str = ""
    for i in s:

        if i >= 'A' and i <= 'Z':
            str += chr(ord(i) + 32)
        else:
            str += i

    return str
    
s = input()
print(to_lower(s))