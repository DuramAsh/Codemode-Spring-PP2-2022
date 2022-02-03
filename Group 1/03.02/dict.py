mydict = {}
mydict2 = dict()

mydict["bmw"] = 39
mydict["mers"] = 124
mydict["audi"] = 80

# for i in mydict.keys():
#     print(i, mydict[i])

keys = mydict.keys()
values = mydict.values()
print(*keys)
print(*values)

mydict['audi'] = 100
mydict['2'] = 34
# mydict[90] = 340

print()
print('-'*20)

for k, v in mydict.items():
    print(k, v)

print()
print('-'*20)

print(*sorted(mydict.items()), sep='\n')