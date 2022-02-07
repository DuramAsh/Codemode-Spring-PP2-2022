l = list(map(int, input().split()))
if all(elem > 0 for elem in l):
    if all(str(elem) == str(elem)[::-1] for elem in l):
        print("Rovnyi")
    else:
        print("Ne rovnyi")
else:
    print("Ne rovnyi")
    

#1
# if all(elem > 0 for elem in l):
#2
# for elem in l:
#     if elem > 0:

#1
# if all(str(elem) == str(elem)[::-1] for elem in l):
#2
# for elem in l:
#     if str(elem) == str(elem)[::-1]:      