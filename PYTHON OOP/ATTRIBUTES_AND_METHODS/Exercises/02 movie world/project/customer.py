
class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.id = id
        self.age = age
        self.rented_dvds = []

    def has_dvd(self, dvd):
        return dvd in self.rented_dvds

    def add_dvd(self, dvd):
        self.rented_dvds.append(dvd)

    def remove_dvd(self, dvd):
        self.rented_dvds.remove(dvd)

    def __repr__(self):
        dvd_names = ', '.join([d.name for d in self.rented_dvds])
        data = f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} " \
               f"rented DVD\'s ({dvd_names})"
        return data
