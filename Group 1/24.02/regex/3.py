import re
passwords = [
	"SDF#$%56bn",
	"987!@YHBv",
	"adilIjaks",
	"Group_1",
	"group-adin",
	"GRUPPA-DYVA",
	"_fgjyDF89",
	"a_zhaPAR2020"
]

s = 'sdfASDF'
b = "DFGHvbn"
c = "AbYmRb"
d = "SUIIIII"

pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.+[_!@#$]).{6,12}'
pattern_2 = r'([a-z]+)([A-Z]+)'

# print(re.search(pattern, s))
# print(re.search(pattern, b))
# print(re.search(pattern, c))
# print(re.search(pattern, d))

for i in passwords:
    if re.search(pattern, i):
        print("Valid")
    else:
        print("nope")