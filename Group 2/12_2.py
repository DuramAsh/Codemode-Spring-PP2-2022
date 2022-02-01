from itertools import accumulate


print(*accumulate([int(i) for i in input().split()]))