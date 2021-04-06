class Software:

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int, type: str = "Express" or "Light"):
        self.name = name
        self.type = type  # ("Express" or "Light")
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption

