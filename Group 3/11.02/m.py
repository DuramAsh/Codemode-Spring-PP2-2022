l = list()
while True:
    s = input()
    if s == '0':
        break
    else:
        dd, mm, yy = s.split()
        l.append( (dd, mm, yy) )
        # () - tuple
        # [] - list
        # {} - dict
for date in sorted(l, key = lambda x: (x[2], x[1], x[0])):
    print(*date)
    # date[0] = dd
    # date[1] = mm
    # date[2] = yy
