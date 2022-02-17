import json

# with open('task.json', 'r') as f:
#     temp = f.read()
#     x = json.loads(temp)

f = open('task.json', 'r')
temp = f.read()

dd = json.loads(temp)

# print(type(dd))



dd['myName'] = 'ourName'
dd['nums'].sort()
dd['heroes']['spider-man'] = 'Andrew'

# for k, v in dd['heroes'].items():
#     print('{}: {}'.format(k, v))

for k, v in dd.items():
    print('{}: {}'.format(k, v))

y = json.dumps(dd, indent=4)
with open('res.json', 'w') as f:
    f.write(y)
