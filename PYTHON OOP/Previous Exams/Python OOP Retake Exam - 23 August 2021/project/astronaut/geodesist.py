from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):

    def __init__(self, name):
        super(Geodesist, self).__init__(name=name, oxygen=50)

