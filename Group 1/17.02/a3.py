import json

dd = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

x = json.dumps(dd, indent=1, sort_keys=True, separators=(',\n ', ': '))
# print(type(x))
# print(x)

f = open('a.json', 'w')
f.write(x)
f.close()