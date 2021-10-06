from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):

    def __init__(self, name: str):
        super(Biologist, self).__init__(name=name, oxygen=70)

    def breathe(self):
        self.oxygen -= 5


