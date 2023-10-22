from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Bird(Animal):
    def make_sound(self):
        return "Tweet!"


def animal_sounds(animals):
    for animal in animals:
        print(animal.name + " says " + animal.make_sound())


dog = Dog("Sharik", 2)
cat = Cat("Barsik", 4)
bird = Bird("Kesha", 1)

animal_sounds([dog, cat, bird])
