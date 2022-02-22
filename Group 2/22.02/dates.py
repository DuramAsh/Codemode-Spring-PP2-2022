import re

dates = [
	'32.01.2022',
	'29.01.2023',
	'04.05.2003',
	'22.14.1901',
	'22/11/1901'
]

# 01.01.1900 - 31.12.2022
# DD MM YYYY
# 01 - 31
# 01 02 03 04 ... 08 09 10 11 12
pattern = r'(0[1-9]|[1-2]\d|3[0-1])(\.|/)(0[1-9]|1[012])[./](19\d{2}|20[0-1]\d|202[012])'

for date in dates:
    if re.match(pattern, date):
        print(f'Date {date} is valid!')
    else:
        print(f'Date {date} is NOT valid!')
        