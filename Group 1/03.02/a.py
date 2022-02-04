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

# генератор массива
arr2 = [i+1 for i in range(10)]

# распечатать массив
print("print: ", *arr2)
# реверс массива
print("Reverse: ", *arr2[::-1])

# сумма масива
print("Sum of array: ", sum(arr2))

# обращение по индексам, найти сабмассив
print(*arr2[0:3], end=" -> ")
print(*arr2[3:])
