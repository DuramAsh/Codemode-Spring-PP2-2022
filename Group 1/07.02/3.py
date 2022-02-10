n = int(input())
d = {}
d['a'] = d['b'] = d['c'] = 0

for _ in range(n):
    words = list(map(str, input().split()))
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j] in 'QWERTYUIOPASDFGHJKLZXCVBNM' and i == 0:
                d['a'] += 1
            elif words[i][j] in 'aeiou' and i == 1:
                d['b'] += 1
            elif words[i][j].isdigit() and i == 2:
                d['c'] += 1
print(*d.values())
