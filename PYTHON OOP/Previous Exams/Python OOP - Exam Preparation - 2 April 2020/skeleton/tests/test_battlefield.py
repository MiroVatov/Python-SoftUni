import unittest

from project.battle_field import BattleField
from project.controller import Controller


class TestBattleFiled(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()

    def test_fight_method(self):
        self.controller.add_player("Advanced", "Miro")
        self.controller.add_card("Trap", "Bombs")
        self.controller.add_player("Advanced", "Ivan")
        self.controller.add_card("Magic", "Nuclear")
        self.controller.add_player_card("Miro", "Bombs")
        self.controller.add_player_card("Ivan", "Nuclear")
        self.assertEqual(self.controller.fight("Miro", "Ivan"), f"Attack user health 250 - Enemy user health 210")

    def test_fight_method_if_someone_is_dead(self):
        self.controller.add_player("Beginner", "Miro")
        self.controller.add_card("Trap", "Bombs")
        self.controller.add_card("Magic", "Beatup")
        self.controller.add_card("Trap", "BrutalKill")
        self.controller.add_player("Advanced", "Ivan")
        self.controller.add_card("Magic", "Nuclear")
        self.controller.add_card("Trap", "Flower")
        self.controller.add_card("Trap", "Napkin")
        self.controller.add_player_card("Miro", "Bombs")
        self.controller.add_player_card("Miro", "Beatup")
        self.controller.add_player_card("Miro", "BrutalKill")
        self.controller.add_player_card("Ivan", "Nuclear")
        self.controller.add_player_card("Ivan", "Flower")
        self.controller.add_player_card("Ivan", "Napkin")

        with self.assertRaises(ValueError):
            self.controller.fight("Miro", "Ivan")


if __name__ == "__main__":
    unittest.main()