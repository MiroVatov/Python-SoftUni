from project.hardware.hardware import Hardware
from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        hardware_already_added = [hard for hard in System._hardware if hard.name == power_hardware.name]
        if not hardware_already_added:
            System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        hardware_already_added = [hard for hard in System._hardware if hard.name == heavy_hardware.name]
        if not hardware_already_added:
            System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [hard for hard in System._hardware if hard.name == hardware_name]
        if not hardware:
            return f"Hardware does not exist"
        hardware = hardware[0]
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)

        try:
            hardware.install(express_software)
            System._software.append(express_software)
        except Exception as exception:
            return exception.args[0]

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [hard for hard in System._hardware if hard.name == hardware_name]
        if not hardware:
            return f"Hardware does not exist"
        hardware = hardware[0]
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)

        try:
            hardware.install(light_software)
            System._software.append(light_software)
        except Exception as exception:
            return exception.args[0]

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        software = [software for software in System._software if software_name == software.name]
        hardware = [hardware for hardware in System._hardware if hardware_name == hardware.name]
        if software and hardware:
            Hardware.uninstall(hardware[0], software[0])
            System._software.remove(software[0])
        else:
            return f"Some of the components do not exist"

    @staticmethod
    def analyze():
        total_hardware_memory = sum([hardware.memory for hardware in System._hardware])
        total_hardware_capacity = sum([hardware.capacity for hardware in System._hardware])
        total_software_memory_used = sum([software.memory_consumption for software in System._software])
        total_software_capacity_used = sum([software.capacity_consumption for software in System._software])

        data = f"System Analysis" + '\n'
        data += f"Hardware Components: {len(System._hardware)}" + '\n'
        data += f"Software Components: {len(System._software)}" + '\n'
        data += f"Total Operational Memory: {int(total_software_memory_used)} / {int(total_hardware_memory)}" + '\n'
        data += f"Total Capacity Taken: {int(total_software_capacity_used)} / {int(total_hardware_capacity)}"
        return data

    @staticmethod
    def system_split():
        data = ''
        for component in System._hardware:
            data += f"Hardware Component - {component.name}" + '\n'
            data += f"Express Software Components: {len([expr for expr in component.software_components if expr.type == 'Express'])}" + '\n'
            data += f"Light Software Components: {len([light for light in component.software_components if light.type == 'Light'])}" + '\n'
            data += f"Memory Usage: {int(sum([memory.memory_consumption for memory in component.software_components]))} / {int(component.memory)}" + '\n'
            data += f"Capacity Usage: {int(sum([capacity.capacity_consumption for capacity in component.software_components]))} / {int(component.capacity)}" + '\n'
            data += f"Type: {component.type}" + '\n'
            if len(component.software_components) > 0:
                data += f"Software Components: {', '.join([comp.name for comp in component.software_components])}"
            else:
                data += "None"
        return data
