class Zebra:
    def __init__(self):
        self.colour = 'white'

    def which_stripe(self):
        if self.colour == 'white':
            print("Полоска белая")
            self.colour = 'black'
        elif self.colour == 'black':
            print("Полоска черная")
            self.colour = 'white'


z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"
