n = int(input())
elements = []
for _ in range(n):
    name, mol, price = input().split()
    elements.append((name, int(mol), int(price.strip('$'))))
print()
print()
for name, mol, price in sorted(elements, key = lambda x: (x[1], x[2], x[0])):
    print(f'{mol} {price}$ {name}')