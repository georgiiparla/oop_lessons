class Person:
    name = 'Jared'
    age = 30


print(Person.name)  # Get an attribute
print(Person.age)

print(getattr(Person, 'name'))  # Get an attribute (another way)
print(getattr(Person, 'age'))

print(getattr(Person, 'money', 'Нет такого атрибута'))  # If no attribute like this
print(getattr(Person, 'money', 100))

print(Person.__dict__)  # Для получения всех атрибутов, содержащихся в классе или в экземпляре класса, применяется
# магический атрибут __dict__.

print(hasattr(Person, 'name'))  # Если имеется необходимость проверить наличие конкретного атрибута в классе, то можете
# воспользоваться функцией hasattr
print(hasattr(Person, 'money'))

Person.money = 100  # Create a new attribute
Person.phone = '+1 202 777 xxx'
print(Person.__dict__)
print(Person.money)
print(Person.phone)

print()

setattr(Person, 'name', 'Vasya')    # Change existing attribute
setattr(Person, 'age', '43')
setattr(Person, 'sex', 'male')
setattr(Person, 'height', '1.88m')  # Create a new attribute
print(Person.__dict__)

print()

delattr(Person, 'age')  # Delete an attribute
print(Person.__dict__)
print()
del Person.money    # Delete an attribute (another way)
print(Person.__dict__)
