class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self, h):
        return f'{self.name} sleeps {h} hours'
    
class Student(Person):
    def __init__(self, name, age, id):
        self.id = id
        super().__init__(name, age)

    def sleep(self):
        return f'{self.name} sleeps bad'

P1 = Person('Bauka', 18)
S1 = Student('Dias', 18, '21B')

# print(P1.name, P1.age)
# print(S1.name, S1.age, S1.id)

print(P1.sleep(8))
print(S1.sleep(4))