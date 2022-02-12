#ans = [next(f) for _ in range(n)]
n = int(input())
ans_gen = (i for i in range(n))
ans_list = [i for i in range(n)]
for i in ans_gen:
    print(i, end=" ")
print(ans_list)
# 1 2 4 8 16 