# Создать класс прямоугольников, а также методы, позволяющие найти
# площадь, периметр, и сравнить 2 прямоугольника, выведя тот,
# у которого
# большая площадь        
from Rec import Rectangle

R1 = Rectangle(4, 3, 'blue')
R2 = Rectangle(3, 6, 'cyan')
R3 = Rectangle(10, 5, 'black')
print(R1.get_area(), R2.get_area())
print(R1.get_perimeter(), R2.get_perimeter())
print(R1.compare_by_area(R2))
