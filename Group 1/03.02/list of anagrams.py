strings = input().split()
result = dict()

for word in strings:
    # make string from arr:
    sorted_w = ''.join(sorted(word))
    if sorted_w not in result:
        result[sorted_w] = [word]
    else:
        result[sorted_w].append(word)
    # print(sorted_w, result[sorted_w])
print(list(result.values()))
