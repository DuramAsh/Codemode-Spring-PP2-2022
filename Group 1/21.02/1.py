# Python regular expressions a.k.a. RegEx
import re

s = 'abcabcabdabffab'
pattern = r'ab'
# print(type(pattern))
print(re.match(pattern, s)) # Начинается ли строка с такого шаблона?
print(re.search(pattern, s)) # Есть ли в строке хоть одно вхождение по такому шаблону?
print(re.findall(pattern, s)) 
# print(re.split(pattern, s)) 
for i in re.finditer(pattern, s):
    print(i.span())
    # print(i.start())
    # print(i.end())
    
    
t = "StudentsA12workersA45employees"
print(re.split(r'A\d+', t))

print(re.sub(r'\d+', "!!", t))