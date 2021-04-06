import unittest
from car_manager.car_manager import Car


class CarTest(unittest.TestCase):

    def setUp(self):
        self.car = Car("a", "b", 1, 4)

    def tearDown(self):
        self.car = None

    def test_init(self):
        self.assertEqual(self.car.make, 'a')
        self.assertEqual(self.car.model, 'b')
        self.assertEqual(self.car.fuel_consumption, 1)
        self.assertEqual(self.car.fuel_capacity, 4)

    def test_make_property(self):
        self.assertEqual(self.car.make, 'a')

    def test_car_make_setter_positive(self):
        self.car.make = 'new_car'
        self.assertEqual(self.car.make, 'new_car')

    def test_car_make_setter_without_parameters(self):

        with self.assertRaises(Exception):
            self.car.make = ''

    def test_car_model_property(self):
        self.assertEqual(self.car.model, 'b')

    def test_car_model_setter_positive(self):
        self.car.model = 'new_model'
        self.assertEqual(self.car.model, 'new_model')

    def test_car_model_setter_without_parameters(self):

        with self.assertRaises(Exception):
            self.car.model = ''

    def test_car_fuel_consumption_property(self):
        self.assertEqual(self.car.fuel_consumption, 1)

    def test_car_fuel_consumption_setter_positive(self):
        self.car.fuel_consumption = 2
        self.assertEqual(self.car.fuel_consumption, 2)

    def test_car_fuel_consumption_set_to_zero_or_negative_number(self):

        with self.assertRaises(Exception):
            self.car.fuel_consumption = -1

    def test_car_fuel_capacity_property(self):
        self.assertEqual(self.car.fuel_capacity, 4)

    def test_car_fuel_capacity_setter_positive(self):
        self.car.fuel_capacity = 6
        self.assertEqual(self.car.fuel_capacity, 6)

    def test_car_fuel_capacity_set_to_zero_or_negative_number(self):

        with self.assertRaises(Exception):
            self.car.fuel_capacity = -3

    def test_car_fuel_amount_property(self):
        self.assertEqual(self.car.fuel_amount, 0)

    def test_car_fuel_amount_setter_positive(self):
        self.car.fuel_amount = 3
        self.assertEqual(self.car.fuel_amount, 3)

    def test_car_fuel_amount_set_to_negative_number(self):

        with self.assertRaises(Exception):
            self.car.fuel_amount = -4

    def test_car_refuel_with_negative_fuel_amount(self):

        with self.assertRaises(Exception):
            self.car.refuel(-2)

    def test_car_refuel_with_positive_amount_of_fuel(self):
        self.car.refuel(2)
        self.assertEqual(self.car.fuel_amount, 2)

    def test_car_fuel_amount_more_than_the_capacity_after_refuel(self):
        self.car.refuel(5)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_car_fuel_amount_less_than_the_capacity_after_refuel(self):
        self.car.refuel(2)
        self.assertEqual(self.car.fuel_amount, 2)

    def test_drive_needed_distance_is_calculated_correctly(self):
        self.car.refuel(4)
        self.car.drive(300)
        result = (300 / 100) * self.car.fuel_consumption
        self.assertEqual(result, 3)

    def test_needed_fuel_for_the_distance_is_more_than_the_car_fuel_amount(self):
        self.car.refuel(2)
        with self.assertRaises(Exception):
            self.car.drive(300)

    def test_needed_fuel_for_the_distance_is_more_than_or_equal_to_the_car_fuel_amount(self):
        self.car.refuel(4)
        self.car.drive(350)
        self.assertEqual(self.car.fuel_amount, 0.5)

    # TODO add Test for drive method, aftr having the distance , calculate the needed fuel for the distance to be covered
    # if needed distance is more than the car fuel amount, raise an exception. Otherwise, decrease the car fuel amount


if __name__ == "__main__":
    unittest.main()
