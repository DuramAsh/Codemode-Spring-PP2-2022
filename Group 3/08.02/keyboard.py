rows = ['qwertyuiop','asdfghjkl','zxcvbnm']
words = input().split()
result = []
for word in words:
    if all(letter in rows[0] for letter in word.lower()):
        result.append(word)
    elif all(letter in rows[1] for letter in word.lower()):
        result.append(word)
    elif all(letter in rows[2] for letter in word.lower()):
        result.append(word)
#print([word for word in words if all(letter in rows[0] for letter in word.lower()) or all(letter in rows[1] for letter in word.lower()) or all(letter in rows[2] for letter in word.lower())])