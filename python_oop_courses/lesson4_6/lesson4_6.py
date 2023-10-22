class Doctor:
    def __init__(self, degree):
        self.degree = degree


class Builder:
    def __init__(self, rank):
        self.rank = rank


class Person(Builder, Doctor):
    def __init__(self, rank, degree):
        super().__init__(rank)
        Doctor.__init__(self, degree)


