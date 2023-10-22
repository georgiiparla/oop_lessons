class Robot:
    def set_name(self, name):
        setattr(self, 'name', name)


    def say_hello(self):
        if hasattr(self, 'name'):
            print(f"Hello, human! My name is {self.name}")
        else:
            print(f"У робота нет имени")


    def say_bye(self):
        print("See u later alligator")


c3po = Robot()
r2d2 = Robot()

c3po.say_hello()
c3po.say_bye()

r2d2.say_hello()
r2d2.say_bye()

c3po.set_name("c3po")
r2d2.set_name("r2d2")


