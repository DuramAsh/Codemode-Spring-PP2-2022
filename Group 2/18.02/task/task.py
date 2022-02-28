import json

file = open("task.json", "r")
temp = file.read()
dictsh =  json.loads(temp)

dictsh["myName"] = "Hehe"

print(dictsh["myName"])

dictsh["nums"] = sorted(dictsh["nums"])

print(dictsh["nums"])

dictsh["heroes"]["Spider-Man"] = "Tom"

print(dictsh["heroes"]["Spider-Man"])

dump = json.dumps(dictsh,indent = 5, sort_keys="True")
filee = open("whatIsThis","w")
filee.write(dump)
filee.close()




