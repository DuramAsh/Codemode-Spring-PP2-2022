dates = []

while True:
    s = input()
    if s == '0':
        break
    print(s)
    print(s.split())
    day, month, year = map(str, s.split())
    dates.append((day, month, year))
    
for date in sorted(dates, key=lambda x: (x[2], x[1], x[0])):
    print(*date)