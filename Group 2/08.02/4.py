n = int(input())
set1, set2 = set(), set()
# l1, l2 = [], []
for _ in range(n):
    src, dst = input().split()
    set1.add(src)
    set2.add(dst)
    # l1.append(src)
    # l2.append(dst)
print(*set2.difference(set1))
# print([i for i in l2 if i not in l1][0])