import unittest
from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):

    def test_hhardware__init__(self):
        self.hardware = Hardware("Server", "Heavy", 5000, 3500)
        self.assertEqual(self.hardware.name, "Server")
        self.assertEqual(self.hardware.type, "Heavy")
        self.assertEqual(self.hardware.capacity, 5000)
        self.assertEqual(self.hardware.memory, 3500)
        self.assertEqual(self.hardware.software_components, [])

    def test_phardware__init__(self):
        self.hardware = Hardware("Docking Station", "Power", 3000, 5500)
        self.assertEqual(self.hardware.name, "Docking Station")
        self.assertEqual(self.hardware.type, "Power")
        self.assertEqual(self.hardware.capacity, 3000)
        self.assertEqual(self.hardware.memory, 5500)
        self.assertEqual(self.hardware.software_components, [])

    def test_install_method_raising_exception_memory_failure(self):   # Memory failure
        self.hardware = Hardware("Server", "Heavy", 50, 200)
        self.software = Software("Linux", "Express", 100, 200)
        with self.assertRaises(Exception, msg="Software cannot be installed") as exc:
            self.hardware.install(self.software)

        self.assertEqual(str(exc.exception), exc.msg)

    def test_install_method_raising_exception_capacity_failure(self):   # Capacity failure
        self.hardware = Hardware("Server", "Heavy", 250, 100)
        self.software = Software("Linux", "Express", 100, 200)
        with self.assertRaises(Exception, msg="Software cannot be installed") as exc:
            self.hardware.install(self.software)

        self.assertEqual(str(exc.exception), exc.msg)

    def test_successful_software_install(self):
        self.hardware = Hardware("Server", "Heavy", 250, 200)
        self.software = Software("Linux", "Express", 50, 100)
        self.hardware.install(self.software)
        self.assertEqual(self.hardware.software_components, [self.software])

    def test_uninstall_software(self):
        self.hardware = Hardware("Server", "Heavy", 250, 200)
        self.software = Software("Linux", "Express", 50, 100)
        self.hardware.install(self.software)
        self.hardware.uninstall(self.software)
        self.assertEqual(self.hardware.software_components, [])

    # def test_power_hardware__init__(self):
    #     self.power_hardware = PowerHardware("SSD", 150, 250)
    #     self.assertEqual(self.power_hardware.name, "SSD")
    #     self.assertEqual(self.power_hardware.type, "Power")
    #     self.assertEqual(self.power_hardware.capacity, 37.5)
    #     self.assertEqual(self.power_hardware.memory, 437.5)
    #     self.assertEqual(self.power_hardware.software_components, [])
    #
    # def test_heavy_hardware__init__(self):
    #     self.heavy_hardware = HeavyHardware("HDD", 600, 300)
    #     self.assertEqual(self.heavy_hardware.name, "HDD")
    #     self.assertEqual(self.heavy_hardware.type, "Heavy")
    #     self.assertEqual(self.heavy_hardware.capacity, 1200)
    #     self.assertEqual(self.heavy_hardware.memory, 225)
    #     self.assertEqual(self.heavy_hardware.software_components, [])


if __name__ == "__main__":
    unittest.main()