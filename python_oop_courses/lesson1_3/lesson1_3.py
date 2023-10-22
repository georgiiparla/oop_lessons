# Помните, что атрибуты класса относятся только к самому классу, и при создании  ЭК эти атрибуты не создаются
# в самом ЭК!!!, а получают ссылку!!! на атрибут класса.

class Person:
    name = 'Ivan'
    age = 30


# man = Person()
# print(man.__dict__)
# print(Person.__dict__)
# print()
# man.name = 'Alex'
# print('Атрибуты ЭК:', man.__dict__)
# print('Атрибуты класса:', Person.__dict__)

guy = Person()
print(guy.name)
guy.name = 'Jake'
print(guy.name)
Person.name = 'Fred'
print(guy.name)
