n = int(input())
check = '@gmail.com'
for i in range(n):
    s = input()
    # if s.endswith(check):
    #     print(s.replace(check,''))
    # if check in s:
    #     print(s.replace(check,''))
    if s.endswith(check):
        print(s[ : len(s) - (len(check))])
        