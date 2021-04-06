from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    @property
    def make_sound(self):
        return "Meow"


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    @property
    def make_sound(self):
        return "Woof!" + "showing teeth"


animals = [Cat("Puhi"), Dog("Woofy")]
for animal in animals:
    print(animal.make_sound)
