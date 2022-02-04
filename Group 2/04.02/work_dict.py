
word = input()
# abbbsdff
d = {}
for i in word:
    if i not in d.keys():
        d[i] = 1
    # if d.get(i, 0) == 0:
    #     d[i] = 1
    else:
        d[i] += 1
        
print(d.items())