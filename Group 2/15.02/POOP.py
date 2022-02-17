class Car:    
    def __init__(self, year, color, VIN, manufacturer):
        self.year = year
        self.color = color
        self.VIN = VIN
        self.manufacturer = manufacturer
    
    def move(self):
        return f'Car {self.VIN} is moving!'
        
    


C1 = Car('2020', 'white', 'KZ201289461293JK', 'Chevrolet')
C2 = Car('1993', 'red', 'JX12789397123', 'Daewoo')
print(C1.color, C2.manufacturer)

print(str('abc').upper())
print(C1.move())