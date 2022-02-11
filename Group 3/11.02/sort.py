#sorted(collection, key, reverse=True/False)
ls = []
n = int(input())
for _ in range(n):
    name, last_name, age = input().split()
    ls.append((name, last_name, int(age)))
for name, last_name, age in sorted(ls):
    print(name, last_name, age)