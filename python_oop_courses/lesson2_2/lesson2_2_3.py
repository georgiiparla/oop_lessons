class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{self.brand} {self.model}'


laptop1 = Laptop('Apple', 'Pro', 150000)
laptop2 = Laptop("Lenovo", 'Air-2', 60000)
