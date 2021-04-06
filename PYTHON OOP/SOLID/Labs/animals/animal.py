class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def get_species(self):
        return self.species

    def make_sound(self):
        if self.species in animals_collection.animals_dict.keys():
            print(f"{self.species}: {self.sound}")


class AnimalsDict:
    def __init__(self):
        self.animals_dict = {}

    def add_animal(self, animal):
        if animal.species in self.animals_dict:
            return f"Animal {animal.species} already in the collection."

        self.animals_dict[animal.species] = animal.sound
        return f"Animal {animal.species} successfully added in the collection."


cat = Animal("Cat", "Meow")
dog = Animal("Dog", "Woof!")
animals_collection = AnimalsDict()
print(animals_collection.add_animal(cat))
print(animals_collection.add_animal(dog))
print(animals_collection.add_animal(dog))
# dog.make_sound()
for an, sound in animals_collection.animals_dict.items():
    print(an, sound)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
