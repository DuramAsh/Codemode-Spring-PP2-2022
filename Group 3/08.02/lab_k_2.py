words = input().replace(',','').replace('?','').replace('!','').replace('.','').split
s = set([word for word in words])
print(len(s))
print(*sorted(s),sep='\n')