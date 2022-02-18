import json
# load, loads
after_edit_file = open('output.json', 'r').read()
dd = json.loads(after_edit_file)
dd['name'] = 'Alikh'
# for key, val in sorted(dd.items()):
#     print(key, val)

file = open('output.json', 'w')
file.write(json.dumps(dd, indent=4))
file.close()