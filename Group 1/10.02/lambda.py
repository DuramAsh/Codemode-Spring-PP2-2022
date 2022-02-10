def sum(n):
    return n + 10

print(sum(5))

function = lambda x: x + 10
summa = lambda a, b, c: a + b + c

print(summa(9, 10, 20))
print(summa(20, 30, 10))

# arr = list(map(lambda x: int(x) * 10, input().split()))
# print(*arr)

dict = {}
dict["bmw"] = 39
dict["mers"] = 124
dict["audi"] = 100

for k, v in dict.items():
    print(k, v)
    
ss = list(dict.items())
ss.sort(key = lambda x: x[1], reverse=True)
# ss.sort()
for i in ss:
    print(*i)    