import unittest
from project.pet_shop import PetShop


class PetShopTest(unittest.TestCase):

    def test_correct__init__(self):
        self.shop = PetShop("Monkey")
        self.assertEqual(self.shop.name, "Monkey")
        self.assertEqual(self.shop.food, {})
        self.assertEqual(self.shop.pets, [])

    def test_incorrect__init__(self):
        self.shop = PetShop("Monkey")
        self.assertNotEqual(self.shop.name, "Donkey")
        self.assertEqual(self.shop.food, {})
        self.assertEqual(self.shop.pets, [])

    def test_add_food_method_raises_error(self):
        self.shop = PetShop("Monkey")
        with self.assertRaises(ValueError) as exc:
            self.shop.add_food("seeds", 0)

        msg = "Quantity cannot be equal to or less than 0"
        self.assertEqual(str(exc.exception), msg)

    def test_add_food_not_in_foods_dict(self):
        self.shop = PetShop("Monkey")
        self.shop.add_food("seeds", 5)
        self.assertEqual(self.shop.food, {"seeds": 5})

    def test_add_food_return_message(self):
        self.shop = PetShop("Monkey")
        msg = f"Successfully added 5.00 grams of seeds."
        self.assertEqual(self.shop.add_food("seeds", 5), msg)

    def test_add_food_method_food_already_in_food_dict(self):
        self.shop = PetShop("Monkey")
        self.shop.add_food("seeds", 5)
        self.shop.add_food("seeds", 5)
        self.assertEqual(self.shop.food, {"seeds": 10})

    def test_add_pet_method(self):
        self.shop = PetShop("Monkey")
        msg = "Successfully added Jerry."
        self.assertEqual(self.shop.add_pet("Jerry"), msg)
        self.assertEqual(self.shop.pets, ["Jerry"])

    def test_add_pet_raises_error(self):
        self.shop = PetShop("Monkey")
        self.shop.add_pet("Jerry")
        with self.assertRaises(Exception) as exc:
            self.shop.add_pet("Jerry")

        msg = "Cannot add a pet with the same name"
        self.assertEqual(str(exc.exception), msg)

    def test_feed_pet_method_pet_not_in_pets_list(self):
        self.shop = PetShop("Monkey")
        with self.assertRaises(Exception) as exc:
            self.shop.feed_pet("pet_food", "Jerry")

        msg = "Please insert a valid pet name"
        self.assertEqual(str(exc.exception), msg)

    def test_feed_pet_method_food_not_in_foods_dict(self):
        self.shop = PetShop("Monkey")
        self.shop.add_pet("Jerry")
        msg = "You do not have pet food"
        self.assertEqual(self.shop.feed_pet("pet food", "Jerry"), msg)

    def test_feed_pet_method_food_quantity_less_than_100(self):
        self.shop = PetShop("Monkey")
        self.shop.add_pet("Jerry")
        self.shop.add_food("seeds", 99)
        self.assertEqual(self.shop.feed_pet("seeds", "Jerry"), "Adding food...")
        self.assertEqual(self.shop.food, {"seeds": 1099.00})

    def test_feed_pet_positive_result(self):
        self.shop = PetShop("Monkey")
        self.shop.add_pet("Jerry")
        self.shop.add_food("seeds", 101)
        self.assertEqual(self.shop.feed_pet("seeds", "Jerry"), "Jerry was successfully fed")
        self.assertEqual(self.shop.food, {"seeds": 1})

    def test__repr__method(self):
        self.shop = PetShop("Monkey")
        self.shop.add_pet("Jerry")
        self.shop.add_pet("Tom")
        msg = "Shop Monkey:\nPets: Jerry, Tom"
        self.assertEqual(self.shop.__repr__(), msg)


if __name__ == "__main__":
    unittest.main()
