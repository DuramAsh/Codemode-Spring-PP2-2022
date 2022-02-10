n = int(input())
domain = '@gmail.com'
for i in range(n):
    email = input()
    if domain in email:
        print(email[ :-10])