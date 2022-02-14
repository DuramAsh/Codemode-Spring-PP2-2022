class Person:

    def __init__(self, gender):
        self.gender = gender


class Student(Person):

    def __init__(self, loan, gender):
        super().__init__(gender)
        self.loan = loan

# class Employee(Person):
#     pass


# class Teacher(Employee):
#     pass


Ernat = Student(2500, 'M')
print(Ernat.loan, Ernat.gender)