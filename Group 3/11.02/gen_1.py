def gen_squares(n, k = 1):
    for i in range(n):
        yield k**2
        k += 1


n = int(input())
#gen = gen_squares(n)
#print(*[next(gen) for i in range(n)])

gen_seq = (i**2 for i in range(1, n + 1))
for i in gen_seq:
    print(i, end=" ")