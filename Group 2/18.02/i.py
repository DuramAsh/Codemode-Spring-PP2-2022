f = open('input.txt', 'r')
x = f.read().split()
print(*x, sep='\n')