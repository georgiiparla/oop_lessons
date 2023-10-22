class Circle:
    def __init__(self, radius):
        if not Circle.is_positive(radius):
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    @staticmethod
    def is_positive(value):
        if value >= 0:
            return True
        else:
            return False

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @staticmethod
    def area(radius):
        return 3.14*radius**2
