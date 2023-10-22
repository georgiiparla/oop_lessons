class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars*100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, dollars):
        if isinstance(dollars, int):
            if dollars >= 0:
                self.total_cents = self.total_cents % 100 + dollars*100
            else:
                print("Error dollars")
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, cents):
        if isinstance(cents, int):
            if 0 <= cents < 100:
                self.total_cents = self.total_cents // 100 * 100 + cents
            else:
                print('Error cents')
        else:
            print('Error cents')

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
print(Bill.total_cents) # 10199
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов
