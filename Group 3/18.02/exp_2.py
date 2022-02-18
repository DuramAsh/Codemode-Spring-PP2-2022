import json
d = {
    "name" : "Bauka",
    "age" : 19,
    "dolgi" : [100, 500, 1000],
    "height" : 181
}
values = json.dumps(d, indent = 4, sort_keys = True)

# file = open('output.json', 'w')
# file.write(values)
# file.close()

with open('output.json', 'w') as file:
    file.write(values)