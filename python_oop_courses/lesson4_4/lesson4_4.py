class Person:
    def breathe(self):
        print('The person is breathing')

    def sleep(self):
        print('The person is sleeping')

    def combo(self):
        self.breathe()
        if hasattr(self, 'walk'):
            self.walk()
        self.sleep()


class Doctor(Person):
    def breathe(self):
        print('The doctor is breathing')

    def sleep(self):
        print('Doctor is sleeping')

    @staticmethod
    def walk(self):
        print('Doctor is walking')


p = Person()
p.combo()

d = Doctor()
d.combo()
