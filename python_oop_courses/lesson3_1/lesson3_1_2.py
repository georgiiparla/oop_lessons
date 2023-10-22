class Vector:
    def __init__(self, *args):
        self.values = [i for i in args if type(i) == int]

    def __str__(self):
        if self.values:
            return f'Вектор{tuple(sorted(self.values))}'
        else:
            return f'Пустой вектор'


v5 = Vector(1, 2, True)
print(v5)
