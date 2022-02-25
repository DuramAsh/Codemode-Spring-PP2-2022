import re
vowels = 'AEIOUaeiou'
cons = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
pattern = r'(?=[%s]([%s]{2,})[%s])' % (cons, vowels, cons)
arr = re.findall(pattern, input())
if arr:
    print(*arr,sep='\n')
else:
    print(-1)

# layout = '%s is cool' % (input())
# layout = f'{input()} is cool'
# print(layout)