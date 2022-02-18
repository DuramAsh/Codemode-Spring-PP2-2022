import json
#dump, dumps
#load, loads

d = {
    "name" : "Bauka",
    "age" : 19,
    "dolgi" : [100, 500, 1000]
}
values = json.dumps(d, indent = 4, sort_keys = True)

file = open('output.json', 'w')
file.write(values)
file.close()

# print(values)
# print(type(values))

#mode = 'r' - read
#       'w' - write
#       'a' - append

