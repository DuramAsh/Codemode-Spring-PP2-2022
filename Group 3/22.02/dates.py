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
for date in dates:
    if re.match(pattern, date):
        print("Yes")
    else:
        print("No")