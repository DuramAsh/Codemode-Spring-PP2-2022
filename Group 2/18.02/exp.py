import json
#dump, dumps
#load, loads
dd = {
    "name" : "Alikh",
    "age" : 18,
    "retakes" : ["Non Stata", "Grant"]
}
# values = json.dumps(dd)
# values = json.dumps(dd)
# print(values)
# print(type(values))
for k, v in json.loads(dd):
    print(k, v)