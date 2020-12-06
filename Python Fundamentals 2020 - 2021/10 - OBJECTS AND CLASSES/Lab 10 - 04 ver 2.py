class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "birds":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        global species_names
        zoo_name = self.name

        if species == "mammal":
            species_names = self.mammals
        elif species == "fish":
            species_names = self.fish
        elif species == "bird":
            species.names = self.birds

        names = ', '.join(species_names)
        return f"{species} in {zoo_name}: {names}"

    def get_total(self):
        return f"Total animals: {self.__animals}"

zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())

for i in range(n):
    species, name = input().split(" ")
    zoo.add_animal(species, name)

species = input()

print(zoo.get_info(species))
print(zoo.get_total())