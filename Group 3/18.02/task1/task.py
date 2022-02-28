import json
# d[nums] = sorted(d[nums])
# d[heroes]["spider_man] = "Peter"
with open('task.json', 'r') as file:
    text = file.read()
    d = json.loads(text)
    d['myName'] = 'Dias'
    d['nums'] = sorted(d['nums'])
    d['heroes']['spider_man'] = 'Peter'

    values = json.dumps(d,indent = 5,sort_keys=True)
    with open('task.json', 'w') as file:
        file.write(values)