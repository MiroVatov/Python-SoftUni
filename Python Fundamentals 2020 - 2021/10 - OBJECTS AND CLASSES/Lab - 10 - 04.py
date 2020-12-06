class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'bird':
            self.birds.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        animals_to_display = []

        if species == 'mammal':
            animals_to_display = self.mammals
        elif species == 'bird':
            animals_to_display = self.birds
        elif species == 'fish':
            animals_to_display = self.fishes
        species = species.capitalize() + "es" if species == "fish" else species.capitalize() + "s"

        return f"{species} in {self.name}: {', '.join(animals_to_display)}\n" \
                f"Total animals: {Zoo.__animals}"

zoo_name = input()
rows_num = int(input())

zoo = Zoo(zoo_name)

for i in range(rows_num):
    species, animal_name = input().split()
    zoo.add_animal(species, animal_name)

required_species = input()

print(zoo.get_info(required_species))