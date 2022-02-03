# list 
arr = []
arr.append("Jaks")
arr.append("Adil")

for i in range(5):
    arr.append(str(i))

for i in arr:
    print(i, end=' ')

print()
print("-"*20)

arr2 = [i+1 for i in range(10)]

print(*arr2)
print(*arr2[0:3])
print(*arr2[::-1])

print(sum(arr2))

print(*arr2[0:3], end=" -> ")
print(*arr2[3:])