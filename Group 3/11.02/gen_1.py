def gen_squares(n, k = 1):
    while k**2 <= n:
        if(k**2 % 2 == 0):
            yield k**2
        k += 1


n = int(input())
#gen = gen_squares(n)
#for i in gen:
#    print(i)

gen_seq = (i**2 for i in range(1, n + 1) if i**2 % 2 == 0 and i**2 < n)
for i in gen_seq:
    print(i, end=" ")