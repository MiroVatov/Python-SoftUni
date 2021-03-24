from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):

    def __init__(self, name, capacity, memory, type='Heavy'):
        super().__init__(name, capacity, memory, type)
        self.name = name
        self.type = type
        self.capacity = capacity * 2
        self.memory = memory * 0.75

