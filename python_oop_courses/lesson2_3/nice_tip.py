# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         return f"Hello, my name is {self.name}," \
#                f"and I am {self.age} years old."
#
#
# persons = [Person('Arcadi', 20), Person('Alex', 40), Person('Susan', 44)]
#
# print(persons)
# print(persons[0].name)
# print(persons[1].age)
# print(persons[2].greet())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}," \
               f"and I am {self.age} years old."


persons = [Person('Arcadi', 20), Person('Alex', 40),
           Person('Susan', 44), Person('Snezhana', 44)]

for prs in persons:
    print(prs.greet())

