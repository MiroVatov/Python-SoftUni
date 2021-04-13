from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):   # NOTE TODO The FreshwaterFish could only live in FreshwaterAquarium!
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name=name, species=species, size=3, price=price)
        self.allowed_aquarium = "FreshwaterAquarium"

    def eat(self):
        self.size += 3

