import json,random
l = list()
with open('names.txt','r') as names:
    for name in names.read().split():
        l.append(name)
# print(l)
dictsh = {}
for i in range(len(l)):
    dictsh[i + 1] = (l[i],random.randint(1,500))

# for a,b in dictsh.items():
#     print(f'{a} = {b}')   
with open('names.json', 'w') as output:
    output.write(json.dumps(dictsh, indent=4)) 

