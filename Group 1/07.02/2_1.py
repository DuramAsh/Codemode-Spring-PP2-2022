n = int(input())
cities = set()
mydict = {}

for _ in range(n):
    a, b = input().split()
    mydict[a] = b
    cities.add(a)
    cities.add(b)

# print(cities)
# print(mydict.keys(), mydict.values())

for city in cities:
    # if mydict.get(city, 0) == 0:
    if city not in mydict.keys():
        print(city)
        break