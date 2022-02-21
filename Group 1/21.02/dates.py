import re

dates = [
	'32.01.2022',
	'29.01.2023',
	'15.05.2003',
	'22.14.1901',
	'22/11/1901'
]

# dates from 01.01.1900 to 31.12.2022

# format: DD.MM.YYYY
# 01 02 03 04 05 06 ... 10 ... 11 12 13 ... 20 .... 30 ... 31
pattern = r'(0[1-9]|[1-2][0-9]|3[01])[./](0[1-9]|1[0-2])(\.|/)(19\d{2}|20[0-1]\d|202[0-2])'

for i in dates:
    if re.match(pattern, i):
        print('Valid year!')
    else:
        print('Not valid year!')