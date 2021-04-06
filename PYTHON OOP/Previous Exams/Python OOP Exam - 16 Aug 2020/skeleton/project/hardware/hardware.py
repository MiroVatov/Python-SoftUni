class Hardware:

    def __init__(self, name: str, capacity: int, memory: int, type: str = "Heavy" or "Power"):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        self.software_components.append(software)

    def uninstall(self, software):
        self.software_components.remove(software)







