n = int(input())
d = {}
for _ in range(n):
    src, dst = input().split()
    d[src] = dst
    
print(*set(d.values()).difference(set(d.keys())))