class Car:
    model = "BMW"
    engine = 1.6

    @staticmethod
    def drive():
        print("Let's go")


a = Car()
b = Car()

Car.drive()
getattr(Car, 'drive')()

a.drive()
b.drive()

# IF LIKE THIS
# class Car:
#   model = "BMW"
#   engine = 1.6
#
#   def drive():
#     print("Let's go")
#
# auto = Car()
# auto.drive()

# THEN ERROR AS DRIVE FUNCTION DOESN'T HAVE A SELF ARGUMENT
# To prevent the error, use @staticmethod decorator
