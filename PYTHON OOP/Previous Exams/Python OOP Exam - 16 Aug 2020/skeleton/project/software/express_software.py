from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption, type="Express"):
        super().__init__(name, capacity_consumption, memory_consumption)
        self.name = name
        self.type = type
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption * 2

