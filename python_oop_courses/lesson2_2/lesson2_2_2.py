class Person:
    def __init__(self, name: str, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hello, my name is {self.name.title()}, and I am {self.age} years old'
