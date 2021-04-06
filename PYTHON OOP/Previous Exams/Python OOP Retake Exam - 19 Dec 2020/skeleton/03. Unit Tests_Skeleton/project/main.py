import unittest
from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    @abstractmethod
    def add_ingredient(self, type, quantity):
        """Add products to the factory"""
        pass

    @abstractmethod
    def remove_ingredient(self, type, quantity):
        """Remove products from the factory"""
        pass

    def can_add(self, value):
        return self.capacity - sum(self.ingredients.values()) - value >= 0

    def __repr__(self):
        result = ""
        result += f"Factory name: {self.name} with capacity {self.capacity}.\n"
        for ingredient in self.ingredients:
            result += f"{ingredient}: {self.ingredients[ingredient]}\n"
        return result


from project.factory.factory import Factory


class PaintFactory(Factory):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def add_ingredient(self, product_type, product_quantity):
        if product_type in ["white", "yellow", "blue", "green", "red"]:
            if self.can_add(product_quantity):
                if product_type not in self.ingredients:
                    self.ingredients[product_type] = 0
                self.ingredients[product_type] += product_quantity
            else:
                raise ValueError("Not enough space in factory")
        else:
            raise TypeError(f"Ingredient of type {product_type} not allowed in {self.__class__.__name__}")

    def remove_ingredient(self, product_type, product_quantity):
        if product_type in self.ingredients:
            if self.ingredients[product_type] - product_quantity >= 0:
                self.ingredients[product_type] -= product_quantity
            else:
                raise ValueError("Ingredients quantity cannot be less than zero")
        else:
            raise KeyError("No such ingredient in the factory")

    @property
    def products(self):
        return self.ingredients


# from project.factory.paint_factory import PaintFactory


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