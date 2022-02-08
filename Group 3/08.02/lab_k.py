words = input()
s = ''
res = set()
for i in range(len(words)):
    if words[i].isalpha(): #[A-Z] and [a-z]
        s += words[i]
    elif words[i] == ' ' or i == len(words) - 1:
        res.add(s)
        s = ''
print(len(res))
print(*sorted(res),sep='\n')