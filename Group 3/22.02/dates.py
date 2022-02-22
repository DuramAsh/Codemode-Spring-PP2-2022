import re

dates = [
	'32.01.2022',# No
	'29.01.2023',# No
	'04.05.2003',# Yes
	'22.14.1901',# No
	'22/11/1901' # Yes
]

# DD MM YYYY
#sep = . /
pattern = r'(0[1-9]|[1-2][0-9]|3[01])[./](0[1-9]|1[0-2])[./](19[0-9]{2}|20[0-1][0-9]|202[0-2])$'
pattern = r'(?P<day>0[1-9]|[1-2][0-9]|3[01])[./](?P<month>0[1-9]|1[0-2])[./](?P<year>19[0-9]{2}|20[0-1][0-9]|202[0-2])$'
# pattern_2 = r'()()()()' # group = 5
for date in dates:
    if re.match(pattern, date):
        # output = re.match(pattern, date).group(0)
        # day = re.match(pattern, date).group(1)
        # month = re.match(pattern, date).group(2)
        # year = re.match(pattern, date).group(3)
        day = re.match(pattern, date).group('day')
        month = re.match(pattern, date).group('month')
        year = re.match(pattern, date).group('year')
        print(day, month, year, sep=':')
        # print("Yes")
    else:
        print("No")