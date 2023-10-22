class BankAccount:
    bank_name = 'Tinkoff Bank'
    address = 'Москва, ул. 2-я Хуторская, д. 38А'

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @classmethod
    def create_account(cls, name, amount):
        return cls(name, amount)

    @staticmethod
    def bank_info():
        return f'{BankAccount.bank_name} is located in {BankAccount.address}'
