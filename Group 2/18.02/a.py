# dict => json : dumps
# json => dict : loads


import json

dd = {
    'name': 'Ernat',
    's_name': "Danial",
    "number_of_fingers": 11,
    "retakes": ['Statistics', 'PP2', 'Physics']
}

x = json.dumps(dd, indent = 4, sort_keys = True)

# print(x)
# print(type(x))

file = open('output.json', 'w')
file.write(x)
file.close()