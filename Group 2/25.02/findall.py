import re
v = "AEIOUaeiou"
c = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"
arr = re.findall(r"(?=[%s]([%s]{2,})[%s])" % (c, v, c), input())
if arr:
    print(*arr, sep='\n')
else:
    print(-1)
    
    
# layout = '%s is boy' % (input())
# layout_format = f'{input()} is boy'
# print(layout)