import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):

    def setUp(self):
        self.card_repository = CardRepository()

    def test__init__(self):
        self.assertEqual(self.card_repository.cards, [])
        self.assertEqual(self.card_repository.count, 0)

    def test_add_card_successful(self):
        self.magic_card = MagicCard("Michelin")
        self.card_repository.add(self.magic_card)
        self.assertEqual(self.card_repository.cards, [self.magic_card])
        self.assertEqual(self.card_repository.count, 1)

    def test_add_card_raise_value_error(self):
        self.magic_card = MagicCard("Michelin")
        self.card_repository.add(self.magic_card)
        with self.assertRaises(ValueError) as exc:
            self.card_repository.add(self.magic_card)
        msg = f"Card {self.magic_card.name} already exists!"
        self.assertEqual(str(exc.exception), msg)

    def test_remove_card_successful(self):
        self.magic_card = MagicCard("Michelin")
        self.magic_card_2 = MagicCard("Dongle")
        self.card_repository.add(self.magic_card)
        self.card_repository.add(self.magic_card_2)
        self.card_repository.remove("Michelin")
        self.assertEqual(self.card_repository.cards, [self.magic_card_2])
        self.assertEqual(self.card_repository.count, 1)

    def test_remove_card_raises_value_error_card_not_in_repository(self):
        self.magic_card = MagicCard("Michelin")
        self.card_repository.add(self.magic_card)
        with self.assertRaises(ValueError) as exc:
            self.card_repository.remove("")
        msg = "Card cannot be an empty string!"
        self.assertEqual(str(exc.exception), msg)

    def test_find_method_finds_the_card(self):
        self.magic_card = MagicCard("Michelin")
        self.magic_card_2 = MagicCard("Dongle")
        self.card_repository.add(self.magic_card)
        self.card_repository.add(self.magic_card_2)
        self.assertEqual(self.card_repository.find("Michelin"), self.magic_card)

    def test_find_method_not_find_card_return_none(self):
        self.magic_card = MagicCard("Michelin")
        self.card_repository.add(self.magic_card)
        self.assertEqual(self.card_repository.find("Dongle"), None)


if __name__ == "__main__":
    unittest.main()