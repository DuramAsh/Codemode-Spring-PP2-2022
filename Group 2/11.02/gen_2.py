def gener(m):
    n = 1
    yield n
    
    for _ in range(m):
        n *= 2
        yield n

n = int(input())
number = gener(n)

for _ in range(n):
    print(next(number), end=' ')