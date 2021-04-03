import unittest

from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor
from project.bunker import Bunker


class BunkerTest(unittest.TestCase):

    def setUp(self):
        self.bunker = Bunker()
        self.survivor_one = Survivor("Johnny", 35)
        self.survivor_two = Survivor("Michael", 28)
        self.survivor_three = Survivor("Norman", 44)
        self.food_supply = FoodSupply()
        self.food_supply_2 = FoodSupply()
        self.water_supply = WaterSupply()
        self.water_supply_2 = WaterSupply()
        self.painkiller = Painkiller()
        self.painkiller_2 = Painkiller()
        self.salve = Salve()
        self.salve_2 = Salve()

    def test_survivor_health_set_to_under_100(self):
        self.survivor_one.health = 20
        self.survivor_one.needs = 20

        self.assertEqual(True, self.survivor_one.needs_healing)
        self.assertEqual(True, self.survivor_one.needs_sustenance)


if __name__ == "__main__":
    unittest.main()
