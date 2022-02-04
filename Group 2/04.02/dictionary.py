mydict = {}
# mydict = dict()

mydict['bmw'] = 39
mydict['audi'] = 100
mydict['lada'] = '2106'

# print(mydict)
keys = mydict.keys()
values = mydict.values()
items = mydict.items()
# print(keys, values, items, sep='\n')
for k, v in items:
    print(k, v)