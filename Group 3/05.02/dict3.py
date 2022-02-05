n = int(input())
d = dict()
for i in range(n):
    name = input()
    d[name] = False

m = int(input())
for i in range(m):
    name = input()
    d[name] = True

print('Good:')
for key, value in d.items():
    if value == True:
        print(key)

print('Bad:')
for key, value in d.items():
    if value == False:
        print(key)

print(d.items())