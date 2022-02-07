def order(sentence):
    arr = [0 for i in range(10)]
    for i in sentence.split():
        for j in i:
            if j.isdigit():
                arr[int(j)] = i
                break
    return ' '.join(i for i in arr if i != 0)

sentence = input()
print(order(sentence))