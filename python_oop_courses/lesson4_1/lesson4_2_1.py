class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(f'Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}')


class Bus(Vehicle):
    pass
