class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @staticmethod
    def breathe():
        print('The person is breathing')


class Doctor(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def breathe(self):
        super().breathe()
        print("Doctor is breathing")


p = Person('Ivan', 'Ivanov')
d = Doctor('Petr', 'Ivanov', 25)
print(p.name, p.surname)
print(d.name, d.surname, d.age)
