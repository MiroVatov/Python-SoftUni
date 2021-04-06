import unittest

from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):

    def setUp(self):
        self.player_repository = PlayerRepository()

    def test__init__(self):
        self.assertEqual(self.player_repository.players, [])
        self.assertEqual(self.player_repository.count, 0)

    def test_add_player_successful(self):
        self.beginner = Beginner("Michelin")
        self.player_repository.add(self.beginner)
        self.assertEqual(self.player_repository.players, [self.beginner])
        self.assertEqual(self.player_repository.count, 1)

    def test_add_player_raise_value_error(self):
        self.beginner = Beginner("Michelin")
        self.player_repository.add(self.beginner)
        with self.assertRaises(ValueError) as exc:
            self.player_repository.add(self.beginner)
        msg = f"Player {self.beginner.username} already exists!"
        self.assertEqual(str(exc.exception), msg)

    def test_remove_player_successful(self):
        self.beginner = Beginner("Michelin")
        self.advanced = Advanced("Dongle")
        self.player_repository.add(self.beginner)
        self.player_repository.add(self.advanced)
        self.player_repository.remove("Michelin")
        self.assertEqual(self.player_repository.players, [self.advanced])
        self.assertEqual(self.player_repository.count, 1)

    def test_remove_player_raises_value_error_card_not_in_repository(self):
        self.beginner = Beginner("Michelin")
        self.player_repository.add(self.beginner)
        with self.assertRaises(ValueError) as exc:
            self.player_repository.remove("")
        msg = "Player cannot be an empty string!"
        self.assertEqual(str(exc.exception), msg)

    def test_find_method_finds_the_player(self):
        self.beginner = Beginner("Michelin")
        self.advanced = Advanced("Dongle")
        self.player_repository.add(self.beginner)
        self.player_repository.add(self.advanced)
        self.assertEqual(self.player_repository.find("Michelin"), self.beginner)

    def test_find_method_not_find_player_return_none(self):
        self.beginner = Beginner("Michelin")
        self.player_repository.add(self.beginner)
        self.assertEqual(self.player_repository.find("Dongle"), None)


if __name__ == "__main__":
    unittest.main()