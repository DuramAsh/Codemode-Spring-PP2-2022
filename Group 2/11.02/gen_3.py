def gener(m, n = 1):
    for _ in range(m):
        yield n
        #print but returning value
        n *= 2
        
# def gener(m, n = 1):
#     for _ in range(m):
#         n *= 2
#         return n
        

n = int(input())
number = gener(n)

# # for _ in range(n):
# #     print(next(number), end=' ')

ans = [next(number) for _ in range(n)]
print(*ans)

# ans = [gener(n)]
# print(ans)
