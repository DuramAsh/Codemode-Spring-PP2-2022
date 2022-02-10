d = {}

d['mers'] = 222
d['bmw'] = 39
d['audi'] = 100

print(*sorted(d.items(), key=lambda x: x[1]))