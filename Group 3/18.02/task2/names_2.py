import json, random
l = list(name for name in open('names.txt','r').read().split())
open('names.json', 'w').write(json.dumps({i:(l[i], random.randint(1, 500)) for i in range(len(l))}, indent= 4))