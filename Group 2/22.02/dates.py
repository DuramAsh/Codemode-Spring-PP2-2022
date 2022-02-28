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
# pattern = r'(?P<day>)[./]()[./]()'
# pattern = r'(0[1-9]|[1-2]\d|3[0-1])(\.|/)(0[1-9]|1[012])[./](19\d{2}|20[0-1]\d|202[012])'

pattern = r'(?P<day>0[1-9]|[1-2]\d|3[0-1])[./](?P<month>0[1-9]|1[012])[./](?P<year>19\d{2}|20[0-1]\d|202[012])'
# ?P<name_of_group>
for date in dates:
    if re.match(pattern, date):
        # print(f'Date {date} is valid!')
        # day = re.search(pattern, date).group(1)
        # month = re.search(pattern, date).group(3)
        # year = re.search(pattern, date).group(4)
        day = re.search(pattern, date).group("day")
        month = re.search(pattern, date).group("month")
        year = re.search(pattern, date).group("year")
        print(day, month, year, sep=':')
    # else:
    #     print(f'Date {date} is NOT valid!')
        