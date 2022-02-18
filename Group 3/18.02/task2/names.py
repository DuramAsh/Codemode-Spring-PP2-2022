import json, random
l = list()
with open('names.txt','r') as names:
    for name in names.read().split():
        l.append(name)
# print(l)