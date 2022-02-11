arr = list()
while True:
    date = input()
    if date == '0':
        break
    else:
        d = date.split()
        print(d)
        arr.append(d[2] + ' ' + d[1] + ' ' + d[0]) #str
for date in sorted(arr):
    date = date.split()
    print(f'{date[2]} {date[1]} {date[0]}')
    # 2002 10 02
    # 2002 10 01
    # after:
    # 2002 10 01
    # 2002 10 02
