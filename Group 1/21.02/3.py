import re
with open("input.txt", "r") as f:
    x = f.read()


# "46.8.156.153:1050@eTJ3io:MYi4VVpzvM"

pattern = r'(?P<ip>^.+):(?P<host>\d{4})@(?P<user>.+):(?P<pass>.*)'

patric = re.compile(pattern)

for match in patric.finditer(x):
    print(match.group("ip"))
    print(match.group("host"))
    print(match.group("user"))
    print(match.group("pass"))