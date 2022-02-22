import re
#ReGex = Regular Expressions

text = """affafsfsa566ababababaaFfsfasfasf424asfab6aabDSababab123ababaababababababa6236afsf47asfaaSsfasfabaababababababaababaSA"""
pattern = r'.' #raw
ls = re.findall(pattern, text)
print(ls)