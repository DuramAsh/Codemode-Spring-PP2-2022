n = int(input())
first = set()
second = set()
for i in range(n):
    a, b = input().split()
    first.add(a)
    second.add(b)
print(*second.difference(first))