pi = 3.14
class Figure:
    def __init__(self, color):
        self.color = color

class Circle(Figure):
    def __init__(self, rad, color):
        self.rad = rad
        super().__init__(color)

    def get_area(self):
        return pi * self.rad ** 2

    def get_len(self):
        return 2 * pi * self.rad

    def compare(self, another_circle):
        if self.get_area() > another_circle.get_area():
            return 'First is bigger'
        else:
            return 'Second is bigger'


class Square(Figure):
    def __init__(self, side, color):
        self.side = side
        super().__init__(color)

    def get_area(self):
        return self.side ** 2

    def get_per(self):
        return 4 * self.side

    def compare(self, another_square):
        if self.get_area() > another_square.get_area():
            return 'First is bigger'
        else:
            return 'Second is bigger'


def compare(circle, square):
    if circle.get_area() > square.get_area():
        return 'Circle is bigger'
    else:
        return 'Square is bigger'



C1 = Circle(5, 'Red')
C2 = Circle(6, 'Green')

S1 = Square(5, 'Yellow')
S2 = Square(6, 'Blue')

print('Circles:')
print(C1.compare(C2))
# print(C2.compare(C1))

print('Squares:')
print(S1.compare(S2))
# print(S2.compare(S1))

print('Comparing square and circle:')
print(compare(C1, S1))
# print(compare(C2, S2))

