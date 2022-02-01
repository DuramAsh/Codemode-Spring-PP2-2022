#Task 1
#Input:
#1 2 3 4 5
#Output:
#1 4 9 16 25

l1 = list(map(int, input().split()))
#for(int i = 0; i < l.size(); ++i){}
#1
for i in range(len(l1)):
    print(l1[i] ** 2, end=' ')
    #end = '\n'
#range(start, end, step)   
print() 
#2
for i in l1:
    print(i ** 2, end=' ')