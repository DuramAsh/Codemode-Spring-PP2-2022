l = list()
while True:
    s = input()
    if s == '0' or s == 0:
        break
    else:
        l.append(s)
print("Finished")
print(*l)