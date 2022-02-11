d = {
    'boys': (5, 18),
    'girls': (7, 20),
    'transgenders': (1, 52),
    'gays': (5, 19),
    'asexuals': (5, 19)
}

# for k, v in sorted(d.items(), key=lambda x: (x[1][0], x[1][1], x[0]), reverse=True):
#     print(k, v)
for i in d.items():
    print(i[0], i[1], i[1][0], i[1][1])