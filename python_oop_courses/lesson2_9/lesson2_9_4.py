# Метод @classmethod также можно использовать в качестве метода для
# создания нового экземпляра класса.

class Car:

    def __init__(self, model, color):
        self.model = model
        self.color = color

    @classmethod
    def get_red_car(cls, model):
        return cls(model, 'red')


car1 = Car.get_red_car('Audi')
print(car1, car1.model, car1.color)

car2 = Car.get_red_car('BMW')
print(car2, car2.model, car2.color)

# Фабричный метод (Factory method) - пораждающий шаблон проектирования, определяющий
# общий интерфейс создания объектов в родительском классе и позволяющий
# изменять создаваемые объекты в дочерних классах.
