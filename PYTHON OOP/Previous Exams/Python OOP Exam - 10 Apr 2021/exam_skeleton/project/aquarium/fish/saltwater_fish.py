from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):  # NOTE TODO  The SaltwaterFish could only live in SaltwaterAquarium!
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name=name, species=species, size=2, price=price)
        self.allowed_aquarium = "SaltwaterAquarium"

    def eat(self):
        self.size += 2
