#sorted(collection, key, reverse=True/False)
ls = []
n = int(input())
for _ in range(n):
    name, last_name, age = input().split()
    ls.append((name, last_name, int(age)))
for name, last_name, age in sorted(ls, key = lambda x: (x[2], x[1], x[0])):
    print(name, last_name, age)