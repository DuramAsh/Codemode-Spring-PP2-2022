numbers = list(map(int, input().split()))
if all(elem > 0 for elem in numbers):
    if all(str(elem) == str(elem)[::-1] for elem in numbers):
        print("Rovnyi")
    else:
        print("Ne rovnyi")
else:
    print("Ne rovnyi")



#1
# if all(elem > 0 for elem in numbers):
#2
# for elem in numbers:
#     if elem > 0:

#1
# if all(str(elem) == str(elem)[::-1] for elem in numbers):
#2
# ok = False
# for elem in numbers:
#     if str(elem) == str(elem)[::-1]:
#       ok = True
#     else:
#       ok = False
#       break