class Car:
    "Класс для определения характеристик машин"
    model = "BMW"
    engine = 1.6

    def drive(instance):
        print("Let's go")

    def color_car(instance):
        print('Вызов цвета машины')


a = Car()
Car.color_car(a) # Вызов цвета машины
Car.drive(a) # Let's go
