# Create a class and check belonging of instances

class Car:
    pass


a = Car()
b = Car()

print(type(a))
print(type(b))

print('Это объект принадлежит классу Car?', isinstance(a, Car))
print('Это объект принадлежит классу Car?', isinstance(b, Car))
print('Это объект принадлежит классу Car?', isinstance('hello', Car))
