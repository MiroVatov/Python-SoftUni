class PlanetRepository:  # It is a repository for planets that await to be explored

    def __init__(self):
        self.planets = []  # list of planets

    def add(self, planet):
        self.planets.append(planet)  # Adds a planet for exploration.

    def remove(self, planet):
        self.planets.remove(planet)  # Removes a planet from the collection

    def find_by_name(self, name: str):
        for planet in self.planets:
            if planet.name == name:
                return planet
        return None

