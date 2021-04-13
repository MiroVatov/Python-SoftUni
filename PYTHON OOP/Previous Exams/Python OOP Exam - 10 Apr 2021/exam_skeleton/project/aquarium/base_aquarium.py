from abc import ABC, abstractmethod

from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity  #  the number of fish an aquarium can have
        self.decorations = []  # contains all the decorations (objects).
        self.fish = []  #  contain all the fish (objects).


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self._name = value

    def calculate_comfort(self):
        return sum([dec.comfort for dec in self.decorations])   # NOTE Returns the sum of each decoration’s comfort in the Aquarium

    def add_fish(self, fish: BaseFish):
        if fish.allowed_aquarium == self.__class__.__name__:
            if len(self.fish) >= self.capacity:
                return f"Not enough capacity."

            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:  # NOTE check if the fish can be searched with its name
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)   # NOTE decoration object

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        data = f"{self.name}:" + '\n'
        data += f"Fish: "
        if len(self.fish) == 0:
            data += "none"
        for f in self.fish:
            data += f"{f.name}" + " "
        data += '\n'
        data += f"Decorations: {len(self.decorations)}" + '\n'
        data += f"Comfort: {self.calculate_comfort()}" + '\n'
        return data
