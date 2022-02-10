# C++ Set - Sorted and Unique
# Python Set - Unique, Random, Unchangable
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(set(l1).union(set(l2)))
print(set(l1).intersection(set(l2)))
print(set(l1).difference(set(l2)))
print(set(l2).difference(set(l1)))