words = input().split() # <- List
result = {}
for word in words:
    sorted_word = ''.join(sorted(word))
    print(sorted_word)
    if sorted_word in result:
        result[sorted_word].append(word)
    else:
        result[sorted_word] = [word]
        
print(list(result.values()))
    