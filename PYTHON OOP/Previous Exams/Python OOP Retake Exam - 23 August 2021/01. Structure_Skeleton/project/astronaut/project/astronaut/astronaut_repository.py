class AstronautRepository:

    def __init__(self):
        self.astronauts = []  #  It is a repository for the astronauts that are on the Space Station

    def add(self, astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
        return None


