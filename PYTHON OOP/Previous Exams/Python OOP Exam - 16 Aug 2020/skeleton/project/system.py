from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.hardware.hardware import Hardware
from project.software.software import Software


def hardware_check(hardware_name):
    for hardware in System._hardware:
        if hardware_name == hardware.name:
            return hardware


def software_check(software_name):
    for software in System._software:
        if software.name == software_name:
            return software


def check_if_hardware_component_exist(hardware_name):
    for hardware in System._hardware:
        if hardware.name == hardware_name:
            return True
    return False


def check_if_software_component_exist(software_name):
    for software in System._software:
        if software.name == software_name:
            return True
    return False


def calculate_total_hardware_memory_and_capacity(total_used_operational_memory, total_hardware_capacity):
    for hardware in System._hardware:
        total_used_operational_memory += hardware.memory
        total_hardware_capacity += hardware.capacity
    return total_used_operational_memory, total_hardware_capacity


def calculate_total_software_memory_and_capacity(total_memory, total_capacity):
    for software in System._software:
        total_memory += software.memory_consumption
        total_capacity += software.capacity_consumption
    return total_capacity, total_memory


def calc_total_memory_of_the_hardware(software_components):
    total_memory_consumption_of_the_installed_software = 0
    for comp in software_components:
        total_memory_consumption_of_the_installed_software += comp.memory_consumption
    return total_memory_consumption_of_the_installed_software


def calc_the_total_capacity_consumption_of_the_software(software_components):
    total_capacity_used_of_the_installed_software_components = 0
    for software in software_components:
        total_capacity_used_of_the_installed_software_components += software.capacity_consumption
    return total_capacity_used_of_the_installed_software_components


class System:

    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        power_hardware = PowerHardware(name, capacity, memory)
        hardware_already_added = [hard for hard in System._hardware if hard.name == power_hardware.name]
        if not hardware_already_added:
            System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        hardware_already_added = [hard for hard in System._hardware if hard.name == heavy_hardware.name]
        if not hardware_already_added:
            System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):

        hardware = hardware_check(hardware_name)
        if not hardware:
            return "Hardware does not exist"

        # TODO Raise Exception if install conditions are not met !!!

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        total_software_capacity_taken = calc_the_total_capacity_consumption_of_the_software(hardware.software_components)
        total_software_memory = calc_total_memory_of_the_hardware(hardware.software_components)

        if total_software_capacity_taken + express_software.capacity_consumption > hardware.capacity or \
                total_software_memory + express_software.memory_consumption > hardware.memory:
            return "Software cannot be installed"

        hardware.install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):

        hardware = hardware_check(hardware_name)
        if not hardware:
            return "Hardware does not exist"

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        total_software_capacity_taken = calc_the_total_capacity_consumption_of_the_software(
            hardware.software_components)
        total_software_memory = calc_total_memory_of_the_hardware(hardware.software_components)

        if total_software_capacity_taken + light_software.capacity_consumption > hardware.capacity or total_software_memory + light_software.memory_consumption > hardware.memory:
            return "Software cannot be installed"

        hardware.install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):

        if not check_if_hardware_component_exist(hardware_name) and not check_if_software_component_exist(software_name):
            return "Some of the components do not exist"

        hardware = hardware_check(hardware_name)
        software = software_check(software_name)
        # if software not in hardware.software_components:
        #     return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():

        total_hard_disk_memory = 0
        total_software_memory = 0
        total_software_capacity_taken = 0
        total_hardware_capacity = 0
        total_hard_disk_memory, total_hardware_capacity = calculate_total_hardware_memory_and_capacity(total_hard_disk_memory, total_hardware_capacity)
        total_software_capacity_taken, total_software_memory = calculate_total_software_memory_and_capacity(total_software_capacity_taken, total_software_memory)
        data = 'System Analysis' + '\n'
        data += f"Hardware Components: {len(System._hardware)}" + '\n'
        data += f"Software Components: {len(System._software)}" + '\n'
        data += f"Total Operational Memory: {int(total_software_memory)} / {int(total_hard_disk_memory)}" + '\n'
        data += f"Total Capacity Taken: {int(total_software_capacity_taken)} / {int(total_hardware_capacity)}"
        return data

    @staticmethod
    def system_split():
        data = ''

        for component in System._hardware:
            number_of_the_installed_express_software_components = [soft for soft in component.software_components if isinstance(soft, ExpressSoftware)]
            number_of_the_installed_light_software_components = [soft for soft in component.software_components if isinstance(soft, LightSoftware)]
            total_memory_consumption_of_the_installed_software = calc_total_memory_of_the_hardware(component.software_components)
            total_memory_of_the_hardware = component.memory
            total_capacity_used_of_all_installed_software_components = calc_the_total_capacity_consumption_of_the_software(component.software_components)  # capacity_consumption
            total_capacity_of_the_hardware = component.capacity

            data += f"Hardware Component - {component.name}" + '\n'
            data += f"Express Software Components: {len(number_of_the_installed_express_software_components)}" + '\n'
            data += f"Light Software Components: {len(number_of_the_installed_light_software_components)}" + '\n'
            data += f"Memory Usage: {int(total_memory_consumption_of_the_installed_software)} / {int(total_memory_of_the_hardware)}" + '\n'
            data += f"Capacity Usage: {int(total_capacity_used_of_all_installed_software_components)} / {int(total_capacity_of_the_hardware)}" + '\n'
            data += f"Type: {component.type}" + '\n'
            if len(component.software_components) > 0:
                data += f"Software Components: {', '.join([software.name for software in component.software_components])}"   # (or 'None' if no software components)
            else:
                data += f"None"
        return data

