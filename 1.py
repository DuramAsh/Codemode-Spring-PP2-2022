arr = []
XOR = 0
n = input()  
if len(n) >= 3:
    n,x = map(int,n.split())
    for i in range(n):
        elem = x + 2*i
        arr.append(elem)
    for i in range(n):
        XOR ^= arr[i] 
    print(XOR)   
else:
    x = int(input())
    for i in range(len(n)):
        elem = int(x + 2*i)
        arr.append(elem)
    for i in range(len(n)):
        XOR ^= arr[i] 
    print(XOR)