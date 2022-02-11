def gen():
    #1
    n = 1
    yield n
    
    #2
    n += 1
    yield n
    
    #3
    n += 1
    yield n
    
x = gen()

print(next(x))
print(next(x))
print(next(x))