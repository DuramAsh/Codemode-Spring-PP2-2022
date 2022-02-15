class Car:
    def __init__(self, manufacturer, color, year):
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
    
    def move(self):
        return 'This car is moving!'
    
    def get_info(self):
        return f'{self.manufacturer}, {self.color}, {self.year}'




C1 = Car("Chevrolet", "white", 2020)
C2 = Car("BMW", "black", 1993)
# print(C1.color, C2.color)
# print(C1.move(), C2.move())

print(C1.get_info())
print(C2.get_info())
C1.color = 'green'
print(C1.get_info())
print(C2.get_info())


# print()
print('abc'.upper())