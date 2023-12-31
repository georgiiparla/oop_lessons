# class ElectricCar:
#     """Класс для создания электромобиля"""
#
#     def __init__(self, maker, model, year, battery_size=70):
#         self.maker = maker
#         self.model = model
#         self.year = year
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Выводит информацию о мощности аккумулятора."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#     def describe_car_info(self):
#         print(f'{self.maker} {self.model} {self.year}'.title())
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# my_tesla.describe_car_info()
# my_tesla.describe_battery()

class Battery:
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar:
    """Класс для создания электромобиля"""

    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year
        self.battery = Battery()

    def describe_car_info(self):
        print(f'{self.maker} {self.model} {self.year}'.title())


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.describe_car_info()
my_tesla.battery.describe_battery()
print(my_tesla.battery.battery_size)
