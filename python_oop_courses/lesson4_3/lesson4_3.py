class Square:
    def get_value(self, a):
        return a * a


class Cube(Square):
    def get_value(self, a):
        return a * a * a


class Power4(Square):
    def get_value(self, a):
        return a * a * a * a
