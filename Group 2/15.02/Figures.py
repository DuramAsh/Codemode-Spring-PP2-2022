# from math import pi
pi = 3.14

class Figure():
    def __init__(self, color):
        pass

class Circle(Figure):
    def __init__(self, radius, color):
        pass

    def get_area(self):
        pass

	def get_arc(self):
		pass

	def compare(self, Circ2):
		pass

	def __mul__(self):

class Square(Figure):
    def __init__(self, length, color):
        pass

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def compare(self, Sq2):
        pass


def compare(Circle1, Square1):
    pass


C1 = Circle('Какие-то параметры')
C2 = Circle('Какие-то параметры')

S1 = Square('Какие-то параметры')
S2 = Square('Какие-то параметры')

print(C1.compare(C2))
print(compare(C2, S2))