from project.hardware.hardware import Hardware


class PowerHardware(Hardware):

    def __init__(self, name, capacity, memory, type='Power'):
        super().__init__(name, capacity, memory, type)
        self.name = name
        self.type = type
        self.capacity = capacity * 0.25
        self.memory = memory * 1.75
