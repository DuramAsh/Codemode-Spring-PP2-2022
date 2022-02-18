import json, random
l = list()
with open('names.txt','r') as names:
    for name in names.read().split():
        l.append(name)
# print(l)

d = dict()
for i in range(len(l)):
    d[i + 1] = (l[i], random.randint(1, 500))

values = json.dumps(d, indent= 4)
with open('names.json', 'w') as file:
    file.write(values)