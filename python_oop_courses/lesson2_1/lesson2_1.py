class Car:
    "Класс для определения характеристик машин"
    model = "VAZ"
    engine = 1.6
    horse_power = 100
    color = ''

    def drive(instance):
        print(f"Let's go {instance.model} {instance.engine}")

    def power(instance):
        print(f'Мощность {instance.model} - {instance.horse_power} лошадиных сил')

    def color(instance):
        print(f'Цвет {instance.model} - {instance.color}')

    def set_values(instance, new_model, new_engine, new_horse_power, new_color):
        instance.model = new_model
        instance.engine = new_engine
        instance.horse_power = new_horse_power
        instance.color = new_color


auto = Car()
auto.drive()  # Let's go VAZ 1.6
auto.model = 'BMW'  # Поменяем машину
auto.drive()  # Let's go BMW 1.6
auto.power()  # Мощность BMW - 100 лошадиных сил
auto.horse_power = 350  # Добавим лошадок к мощности
auto.power()  # Мощность BMW - 350 лошадиных сил
auto.set_values('AUDI', 5, 300, 'blue')
auto.drive()  # Let's go AUDI 5
auto.power()  # Мощность AUDI - 300 лошадиных сил