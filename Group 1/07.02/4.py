# enumerate
arr = ["Danial", "Ernat", "Aibergen"]
arr2 = ["Darina", "Lera", "Adema"]

for i, j in enumerate(arr):
    print(i, j)
print('-'*20)
for i in range(len(arr)):
    print(i, arr[i])
    
for i, j in zip(arr, arr2):
    print(i, j)
    
