import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):

    def setUp(self):
        self.magic_card = MagicCard("Pinokio")

    def test_magic_card__init__(self):
        self.assertEqual(self.magic_card.name, "Pinokio")
        self.assertEqual(self.magic_card.damage_points, 5)
        self.assertEqual(self.magic_card.health_points, 80)

    def test_magic_card__init__with_empty_name_raises_value_error(self):
        with self.assertRaises(ValueError) as exc:
            self.magic_card.name = ''
        msg = "Card's name cannot be an empty string."
        self.assertEqual(str(exc.exception), msg)

    def test_magic_card__init__with_damage_points_below_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as exc:
            self.magic_card.damage_points = -2
        msg = "Card's damage points cannot be less than zero."
        self.assertEqual(str(exc.exception), msg)

    def test_magic_card__init__with_health_points_below_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as exc:
            self.magic_card.health_points = -2
        msg = "Card's HP cannot be less than zero."
        self.assertEqual(str(exc.exception), msg)


if __name__ == "__main__":
    unittest.main()
