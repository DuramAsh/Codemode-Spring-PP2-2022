# Создать класс прямоугольников, где будет описан какой-либо
# прямоугольник, а также добавим функцию для нахождения его площади
# периметра, изменения его цвета

# class Rectangle:
#     def __init__(self, width, height, color):
#         self.width = width
#         self.height = height
#         self.color = color

#     def get_area(self):
#         return self.width * self.height

#     def get_perimeter(self):
#         return 2 * self.width + 2 * self.height

#     def change_color(self, color):
#         self.color = color

#     def compare_areas(self, R):
#         if self.get_area() > R.get_area():
#             return self.get_area()
#         else:
#             return R.get_area()

from rec_class import *


def compare_area2(pryam1, pryam2):
    return pryam1.get_area() > pryam2.get_area()


R1 = Rectangle(400, 30, 'blue')
R2 = Rectangle(50, 100, 'black')
# print(R1.height * R1.width)
# print(R1.get_area())
# print(R1.get_perimeter())
# R1.color = 'red' # ТАК ДЕЛАТЬ ПЛОХО!!!
# print(R1.color)
# R1.change_color('dasljfljasldkf')
# print(R1.color)

# is_bigger = compare_area2(R1, R2)
is_bigger = R1.compare_areas(R2)
# set1.intersection(set2)
print(is_bigger)