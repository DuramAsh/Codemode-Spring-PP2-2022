# 1 - Наследование
# 2 - Полиморфизм
# 3 - Инкапсуляция

class Student:
    def __init__(self, name, GPA, cs, id):
        self.__name = name
        self.__GPA = GPA
        self.__cs = cs
        self.__id = id
        
    def chalit(self, hours):
        print(f'{self.__name} is challing for {hours} hours')
        
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_GPA(self, GPA):
        self.GPA = GPA
        
    

S1 = Student('Nurback', 3.667, 10, '21B030308')
print(S1.get_name())
S1.set_name('MLG')
print(S1.get_name())