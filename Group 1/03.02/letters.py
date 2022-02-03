# number of letters
s = input()
dict = {}
for i in s:
    if i not in dict.keys():
        dict[i] = 1
    else:
        dict[i] += 1
    print(i, dict[i])
print(*dict.items())
    