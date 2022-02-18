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

values = json.dumps(dd, indent=4, sort_keys = True, separators = (",", ':'))
# print(values)

file = open('values_from_a3.json', 'w') # write
file.write(values)
file.close()