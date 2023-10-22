class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False


class Employee(Person):
    def is_employee(self):
        return True
