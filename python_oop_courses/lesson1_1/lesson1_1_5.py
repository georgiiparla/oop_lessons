class Car:
    model = "BMW"
    engine = 1.6


a = Car()
b = Car()

print(a.model)
print(b.model)

b.model = "VAZ"  # Изменяем значение атрибута model в ЭК
b.color = 'white'  # Добавляем новый атрибут в ЭК
print(b.model, b.color)  # Вывод: VAZ white

