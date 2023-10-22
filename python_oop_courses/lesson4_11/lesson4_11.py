from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


'''Так зачем же нам нужны абстрактные методы? Наследование от абстрактных классов позволяет создавать классы, 
которые являются конкретными реализациями абстрактного класса. Это позволяет нам создавать классы, которые имеют 
общие методы и свойства, но могут реализовывать их по-разному.
Абстрактные классы позволяют определить общий интерфейс для всех дочерних классов, которые будут использовать 
наш абстрактный класс. Все дочерние классы должны будут обязательно иметь реализацию каждого абстрактного метода, 
поэтому мы точно будем уверены, что во всех классах, созданных на основе абстрактного класса, 
будет иметься реализация абстрактных методов.'''
