s = input().split()

arr = [0 for i in range(10)]
# s = is2 Thi1s T4estaaaaa 3a
# [0 thi1 is2 a3 wo4 0 0]
for word in s:
    for i in word:
        if i.isdigit():
            arr[int(i)] = word
            break
# res = ' '.join([i for i in arr if i != 0])
res = ""
for i in arr:
    if i != 0:
        res += str(i) + ' '
print(res)