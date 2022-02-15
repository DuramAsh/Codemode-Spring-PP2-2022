class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_per(self):
        return 2 * (self.length + self.width)

    def compare(self, r2):
        if self.get_area() > r2.get_area():
            return f'First is bigger'
        else:
            return f'Second is bigger'

r1 = Rectangle(3, 6)
r2 = Rectangle(5, 10)

print(r1.get_area(), r2.get_area())
print(r1.get_per(), r2.get_per())

print(r1.compare(r2))
print(r2.compare(r1))