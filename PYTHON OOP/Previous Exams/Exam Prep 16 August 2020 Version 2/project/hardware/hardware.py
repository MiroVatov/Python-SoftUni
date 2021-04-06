from project.software.software import Software


class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type  # NOTE Test both types of hardware ("Heavy" or "Power")
        self.capacity = capacity  # NOTE Test both capacity types of hardware ("Heavy" or "Power")
        self.memory = memory
        self.software_components = []
        self.memory_used = 0
        self.capacity_used = 0

    def install(self, software: Software):

        if self.memory_used + software.memory_consumption > self.memory \
                or self.capacity_used + software.capacity_consumption > self.capacity:
            raise Exception("Software cannot be installed")
            # NOTE create both type of software -->> (Express and Light) / Create both types of hardware as well

        self.software_components.append(software)  # Test successful and unsuccessful installation
        self.memory_used += software.memory_consumption
        self.capacity_used += software.capacity_consumption

    def uninstall(self, software: Software):
        self.software_components.remove(software)
        self.memory_used -= software.memory_consumption
        self.capacity_used -= software.capacity_consumption



