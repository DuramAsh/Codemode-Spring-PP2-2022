import re
#search - first occurance
#n_turdalin@kbtu.kz
#search(kbtu.kz) - true
#search(^kbtu.kz) - false
#search(kbtu.kz$) - true

#match - first occurance, from the begining
#n_turdalin@kbtu.kz
#match(kbtu.kz)
text = """zaffafsfsa566ababababaaFfsfasfasf424asfab6aabDSababab123ababaababababababa6236afsf47asfaaSsfasfabaababababababaababaSA"""
pattern = r'ab' #a, b, e, f, g, h
# print(re.search(pattern, text))
# print(re.match(pattern, text))

# for i in re.finditer(pattern, text):
#     print(i.span())
#     print(i.start())
#     print(i.end())


#Find index of first accurance
print(re.search(pattern, text).start()) 