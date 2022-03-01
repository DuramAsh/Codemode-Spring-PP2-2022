import re

date = input()

thirty = ['04', '06', '09', '11']

def leap(year):
    if int(year) % 400 == 0 and int(year) % 100 == 0:
        return True
    else:
        return False

def day(month, day):
    return False if month in thirty and int(day) == 31 else True

def check(date):
    global d, m, y
    d, m, y = re.split(r'[:;/.]', date)
    if leap(y):
        if m == '02':
            return True if int(d) != 29 else False
        else:
            day(m, d)
    else:
        if m == '02':
            return True if int(d) < 30 else False
        else:
            day(m, d)

# check(date)

pattern = r'(0[1-9]|[1-2][0-9]|3[01])[;:./](0[1-9]|1[0-2])[;:./](19[0-9][0-9]|20[0-9][0-9]|2100)'

if re.search(pattern, date):
    if check(date):
        # print(f'Year: {y}')
        pass
    else:
        print(-1)
else:
    print(-1)