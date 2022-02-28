# loads
import json

with open('a.json', 'r') as f:
    x = f.read()

# print(type(x))
dd = json.loads(x) 

print(type(dd))
print(*dd.keys())
print(*dd.values(), sep='\n')