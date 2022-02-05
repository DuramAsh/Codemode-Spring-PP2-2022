word = input()
letter = input()
arr = []
for i in range(len(word)):
    if word[i] == letter:
        arr.append(i)
if len(arr) == 1:
    print(arr[0])
else:
    print(arr[0],arr[ len(arr) - 1  ])