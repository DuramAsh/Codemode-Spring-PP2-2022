# Создать класс прямоугольников, где будет описан какой-либо
# прямоугольник, а также добавим функцию для нахождения его площади
# периметра, изменения его цвета

class Rectangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color



R1 = Rectangle(40, 30, 'blue')
print(type(R1))