# OOP - Object Oriented Programming
#У каждого есть что: Имя, Возраст, Гендер
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        return f'{self.name} is {self.age} years old. Gender : {self.gender}'


P1 = Person('Dias', 18, 'Male')
P2 = Person('Ertugan', 17, 'Male')
# print(P1.info(), P2.info(), sep = '\n')

print(P1.info())
