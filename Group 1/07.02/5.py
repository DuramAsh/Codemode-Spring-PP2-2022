# double array
# arr = [[0 for i in range(5)] for i in range(5)]

arr = []
for _ in range(5):
    ll = []
    for i in range(5):
        ll.append(i+1)
    arr.append(ll)

# for i in arr:
#     print(*i)
    
for i in arr:
    for j in i:
        print(j, end=' ')
    print()
    
lll = [i+1 for i in range(10)]
print(*lll)