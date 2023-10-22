# https://www.geeksforgeeks.org/defaultdict-in-python/
class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance = amount

    def deposit(self, amount):
        self.__balance += amount

    def payment(self, amount):
        if amount > self.__balance:
            print('Не хватает средств на балансе. Пополните счет')
            return False
        else:
            self.__balance = self.__balance - amount
            return True


class Cart:
    def __init__(self, user: User):
        self.user = user
        self.goods = {}
        self.__total = 0

    def add(self, product: Product, number=1):
        if product in self.goods.keys():
            self.goods[product] = self.goods[product] + number
            self.__total = self.__total + product.price * number
        else:
            self.goods[product] = number
            self.__total = self.__total + product.price * number

    def remove(self, product: Product, number=1):
        if self.goods:
            if 0 <= number <= self.goods[product]:
                self.goods[product] = self.goods[product] - number
                self.__total = self.__total - product.price * number
            else:
                self.__total = self.__total - product.price * self.goods[product]
                self.goods.pop(product)

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        print('---Your check---')
        for name, price, value in sorted([(key.name, key.price, value) for key, value in self.goods.items()]):
            print(f'{name} {price} {value} {value * price}')
        print(f'---Total: {self.total}---')


billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user)  # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total)  # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order()  # Заказ оплачен
print(cart_billy.user.balance)  # 20
