import json as js

file = open('movies.json', 'r')
temp = file.read()
d = js.loads(temp)

d['movies'][1]['imdb'] = 200.0

to_load = js.dumps(d, indent=4)
with open('output.json', 'w') as output:
    output.write(to_load)