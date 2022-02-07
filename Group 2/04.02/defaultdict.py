from collections import defaultdict
# def zero():
#     return 500
d = defaultdict(int)
word = input()
for letter in word:
    d[letter] += 1
# print(*d.items())
for key,v in d.items():
    print(key,v)