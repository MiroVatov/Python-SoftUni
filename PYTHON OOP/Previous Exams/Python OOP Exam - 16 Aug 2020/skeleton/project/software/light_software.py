from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption, type="Light"):
        super().__init__(name, capacity_consumption, memory_consumption)
        self.name = name
        self.type = type
        self.capacity_consumption = capacity_consumption * 1.50
        self.memory_consumption = memory_consumption * 0.50

