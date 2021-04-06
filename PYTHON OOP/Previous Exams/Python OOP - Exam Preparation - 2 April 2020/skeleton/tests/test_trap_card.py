import unittest

from project.card.trap_card import TrapCard


class TestMagicCard(unittest.TestCase):

    def setUp(self):
        self.trap_card = TrapCard("Pinokio")

    def test_trap_card__init__(self):
        self.assertEqual(self.trap_card.name, "Pinokio")
        self.assertEqual(self.trap_card.damage_points, 120)
        self.assertEqual(self.trap_card.health_points, 5)

    def test_trap_card__init__with_empty_name_raises_value_error(self):
        with self.assertRaises(ValueError) as exc:
            self.trap_card.name = ''
        msg = "Card's name cannot be an empty string."
        self.assertEqual(str(exc.exception), msg)

    def test_trap_card__init__with_damage_points_below_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as exc:
            self.trap_card.damage_points = -2
        msg = "Card's damage points cannot be less than zero."
        self.assertEqual(str(exc.exception), msg)

    def test_trap_card__init__with_health_points_below_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as exc:
            self.trap_card.health_points = -2
        msg = "Card's HP cannot be less than zero."
        self.assertEqual(str(exc.exception), msg)


if __name__ == "__main__":
    unittest.main()
