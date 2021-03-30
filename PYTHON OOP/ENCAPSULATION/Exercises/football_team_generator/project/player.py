class Player:

    def __init__(self, name: str, endurance: int, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @property
    def endurance(self):
        return self.__endurance

    @property
    def sprint(self):
        return self.__sprint

    @property
    def dribble(self):
        return self.__dribble

    @property
    def shooting(self):
        return self.__shooting

    @property
    def passing(self):
        return self.__passing

    @name.setter
    def name(self, value):
        self.__name = value

    @endurance.setter
    def endurance(self, value):
        self.__endurance = value

    @sprint.setter
    def sprint(self, value):
        self.__endurance = value

    @dribble.setter
    def dribble(self, value):
        self.__dribble = value

    @passing.setter
    def passing(self, value):
        self.__passing = value

    @shooting.setter
    def shooting(self, value):
        self.__shooting = value

    def __str__(self):
        data = f"Player: {self.name}" + '\n'
        data += f"Endurance: {self.endurance}" + '\n'
        data += f"Sprint: {self.sprint}" + '\n'
        data += f"Dribble: {self.dribble}" + '\n'
        data += f"Passing: {self.passing}" + '\n'
        data += f"Shooting: {self.shooting}" + '\n'
        return data
