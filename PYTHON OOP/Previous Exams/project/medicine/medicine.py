
class Medicine:

    def __init__(self, health_increase: int):
        self.__health_increase = health_increase

    @property
    def health_increase(self):
        return self.__health_increase

    @health_increase.setter
    def health_increase(self, value):
        if value < 0:
            raise ValueError("Health increase cannot be less than zero.")
        self.__health_increase = value

    def apply(self, survivor):
        survivor.health += self.health_increase
        if survivor.health > 100:
            survivor.health = 100
