class Person:
    def __init__(self, name):
        self.name = name
        
    def eat(self, food):
        print(f'{self.name} eats {food}')


class Student(Person):
    def __init__(self, GPA, name):
        self.GPA = GPA
        super().__init__(name)
        
    def eat(self, food):
        print(f'{self.name} goes to ashana and eats {food}')

# S1 = Student(5.0, 'Bakhredin')
S2 = Student('3.667', 'Nurback')
S2.eat('Hlebushek')












# Unordered_set(rem_dub) ->
# set(rem_dub, sort ASC) ->
# ultra_set(rem_dub, sort ASC, washes_plates)