from project.vehicle import Vehicle
import unittest


class VehicleTest(unittest.TestCase):

    def setUp(self):
        Vehicle.DEFAULT_FUEL_CONSUMPTION = 1.25
        self.car = Vehicle(100.0, 120.0)
        # self.car.capacity = self.car.fuel
        # self.car.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION

    def test_init(self):
        self.assertEqual(self.car.fuel, 100.0)
        self.assertEqual(self.car.capacity, 100.0)
        self.assertEqual(self.car.horse_power, 120.0)
        # self.assertEqual(self.car.capacity, self.car.fuel)
        # self.assertEqual(self.car.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_method_raises_exception(self):
        with self.assertRaises(Exception) as exp:
            self.car.drive(90)
        self.assertEqual(exp.exception.args[0], "Not enough fuel")

    def test_drive_method_is_not_throwing_exception(self):
        self.car.drive(80)
        self.assertEqual(self.car.fuel, 0)

    def test_refuel_method_raises_exception(self):
        with self.assertRaises(Exception) as exp:
            self.car.refuel(20)
        self.assertEqual(exp.exception.args[0], "Too much fuel")

    # def test_refuel_method_is_not_throwing_exception(self):
    #     self.car.drive(40)
    #     self.car.refuel(10)
    #     self.assertEqual(self.car.fuel, 60)

    def test_refuel_method_is_not_throwing_exception(self):
        self.car.refuel(0)
        self.assertEqual(self.car.fuel, 100)

    def test_string_method_displays_the_correct_result(self):
        result = self.car.__str__()
        self.assertEqual(result, f"The vehicle has {self.car.horse_power} horse power with {self.car.fuel} fuel left and {self.car.fuel_consumption} fuel consumption")


if __name__ == "__main__":
    unittest.main()


