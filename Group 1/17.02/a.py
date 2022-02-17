import json

dd = {
    'name': 'Ernat',
    's_name': "Danial",
    "number_of_fingers": 11,
    "retakes": ['Statistics', 'PP2', 'Physics']
}

x = json.dumps(dd)

print(x)
print(type(x))