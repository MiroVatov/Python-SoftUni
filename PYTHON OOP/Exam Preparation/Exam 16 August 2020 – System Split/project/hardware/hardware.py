class Hardware:

    def __init__(self, name: str, capacity: int, memory: int, type: str = "Heavy" or "Power"):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        total_used_memory = software.memory_consumption + sum([soft.memory_consumption for soft in self.software_components])
        total_used_capacity = software.capacity_consumption + sum([soft.capacity_consumption for soft in self.software_components])
        if total_used_memory > self.memory or total_used_capacity > self.capacity:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software):
        self.software_components.remove(software)







