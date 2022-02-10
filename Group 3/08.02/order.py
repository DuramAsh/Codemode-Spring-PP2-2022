words = input().split()
result = [0 for _ in range(len(words))]
for word in words:
    for letter in word:
        if letter.isdigit():
            result[int(letter)] = word
            break
print(' '.join([word for word in result]))