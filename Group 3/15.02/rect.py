from Rec import Rectangle

r1 = Rectangle(3, 6)
r2 = Rectangle(5, 10)
r3 = Rectangle(6, 7)

print(r1.get_area(), r2.get_area())
print(r1.get_per(), r2.get_per())

print(r1.compare(r2)) # self = r1
print(r2.compare(r1)) # self = r2
print(r3.compare(r1)) # self = r3
print(r3.compare(r2)) # self = r3