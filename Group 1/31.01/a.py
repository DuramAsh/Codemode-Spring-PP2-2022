x = 5;
y = '5';
print(type(x))
print(type(y))



x = str(3)
print(x + " students")

arr = []
# for(int i=1; i<5; i+=2)

for i in range(5):
    arr.append(i+1)


for i in range(len(arr)):
    print(arr[i])

for i in arr:
    print(i, end=" ")

print()
print("-"*20)

x = 5

def sum_arr():
    global sum
    sum = 0
    for i in arr:
        sum += i
    return sum

sum_arr()
print(sum)

print(8//3)
print(8%3)
print(5**2)
