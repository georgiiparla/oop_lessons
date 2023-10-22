class NewInt(int):
    def __init__(self, number):
        self.number = number

    def repeat(self, n=2):
        return f'{self.number}' * n

    def to_bin(self):
        return bin(self.number)[2:]


a = NewInt(9)
print(a.repeat())  # печатает число 99
d = NewInt(a + 5)
print(d.repeat(3)) # печатает число 141414
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin()) # печатает 100011 - двоичное представление числа 35

