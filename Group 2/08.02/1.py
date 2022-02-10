arr1 = list(map(str, input().split()))
arr2 = [0 for _ in range(10)]
# for _ in range(10):
#     arr2.append(0)

for word in arr1:
    for character in word:
        # if ''.join(j).isdigit():
        if character.isdigit():
            arr2[int(character)] = word
# print(*arr2)
print(*[word for word in arr2 if word != 0])
            