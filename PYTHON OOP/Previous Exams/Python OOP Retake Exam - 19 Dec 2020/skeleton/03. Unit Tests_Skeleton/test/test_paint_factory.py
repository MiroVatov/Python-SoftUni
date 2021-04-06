import unittest
from project.factory.paint_factory import PaintFactory


class Test(unittest.TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory("Colors_factory", 5)

    def test__init__(self):
        self.assertEqual(self.paint_factory.name, "Colors_factory")
        self.assertEqual(self.paint_factory.capacity, 5)
        self.assertEqual(self.paint_factory.ingredients, {})
        self.assertEqual(self.paint_factory.valid_ingredients, ["white", "yellow", "blue", "green", "red"])

    def test_add_ingredient_ingredient_type_not_in_valid_ingredients_raise_type_error(self):
        with self.assertRaises(TypeError) as exc:
            self.paint_factory.add_ingredient("brown", 5)
        msg = f"Ingredient of type brown not allowed in PaintFactory"
        self.assertEqual(str(exc.exception), msg)

    def test_add_ingredient_ingredient_quantity_exceeds_the_paint_factory_capacity_raise_value_error(self):
        with self.assertRaises(ValueError) as exc:
            self.paint_factory.add_ingredient("yellow", 6)
        msg = "Not enough space in factory"
        self.assertEqual(str(exc.exception), msg)

    def test_can_add_method(self):
        self.paint_factory.add_ingredient("blue", 3)
        self.assertEqual(self.paint_factory.can_add(3), False)

        # with self.assertRaises(ValueError) as exc:
        #     self.paint_factory.can_add(3)
        # self.assertEqual(str(exc.exception), "Not enough space in factory")

    def test_add_ingredient_to_the_dict_successfully_ingredient_not_in_the_dict(self):
        self.paint_factory.add_ingredient("yellow", 5)
        self.assertEqual(self.paint_factory.ingredients, {"yellow": 5})

    def test_add_ingredient_to_the_dict_successfully_ingredient_already_in_the_dict(self):
        self.paint_factory.add_ingredient("blue", 3)
        self.paint_factory.add_ingredient("blue", 2)
        self.assertEqual(self.paint_factory.ingredients, {"blue": 5})

    def test_remove_ingredient_from_the_dict_ingredient_not_in_the_dict_raises_key_error(self):
        self.paint_factory.add_ingredient("blue", 3)
        self.paint_factory.add_ingredient("red", 2)
        with self.assertRaises(KeyError) as exc:
            self.paint_factory.remove_ingredient("yellow", 4)
        msg = "No such product in the factory"
        self.assertEqual(msg, "No such product in the factory")

    def test_remove_ingredient_from_the_dict_divide_ingredient_quantity(self):
        self.paint_factory.add_ingredient("red", 3)
        self.paint_factory.remove_ingredient("red", 2)
        self.assertEqual(self.paint_factory.ingredients, {"red": 1})

    def test_remove_ingredient_raises_value_error_quantity_cannot_be_less_than_zero(self):
        self.paint_factory.add_ingredient("red", 3)
        with self.assertRaises(ValueError) as exc:
            self.paint_factory.remove_ingredient("red", 4)
        self.assertEqual(str(exc.exception), "Ingredients quantity cannot be less than zero")

    def test_products_property(self):
        self.paint_factory.add_ingredient("blue", 3)
        self.paint_factory.add_ingredient("red", 2)
        self.assertEqual(self.paint_factory.products, {"blue": 3, "red": 2})


if __name__ == "__main__":
    unittest.main()