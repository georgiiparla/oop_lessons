class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def public_call(self):
        self.__print_private_data()

    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 100000, 45484564654)
print(dir(account1))  # просмотр атрибутов нашего экземпляра класса
print(account1._BankAccount__balance)
print(account1._BankAccount__name)
print(account1._BankAccount__passport)
account1._BankAccount__print_private_data()
