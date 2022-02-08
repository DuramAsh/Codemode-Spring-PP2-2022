words = input().split()
d = dict()
for word in words:
    for letter in word:
        if letter.isdigit():
            d[int(letter)] = word
for k, v in sorted(d.items()):
    print(v, end=' ')