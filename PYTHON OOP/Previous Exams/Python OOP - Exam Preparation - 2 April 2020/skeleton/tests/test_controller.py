import unittest

from project.controller import Controller


class TestController(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()

    def test__init__(self):
        self.assertEqual(self.controller.player_repository.players, [])
        self.assertEqual(self.controller.player_repository.count, 0)
        self.assertEqual(self.controller.card_repository.cards, [])
        self.assertEqual(self.controller.card_repository.count, 0)

    def test_add_player_beginner(self):
        result = self.controller.add_player("Beginner", "Miro")
        self.assertEqual(result, f"Successfully added player of type Beginner with username: Miro")
        self.assertEqual(self.controller.player_repository.count, 1)

    def test_add_player_advanced(self):
        result = self.controller.add_player("Advanced", "Miro")
        self.assertEqual(result, f"Successfully added player of type Advanced with username: Miro")
        self.assertEqual(self.controller.player_repository.count, 1)

    def test_add_card_magic(self):
        result = self.controller.add_card("Magic", "Kill")
        self.assertEqual(result, f"Successfully added card of type MagicCard with name: Kill")
        self.assertEqual(self.controller.card_repository.count, 1)

    def test_trap_card(self):
        result = self.controller.add_card("Trap", "Bombs")
        self.assertEqual(result, f"Successfully added card of type TrapCard with name: Bombs")
        self.assertEqual(self.controller.card_repository.count, 1)

    def test_add_player_card_success(self):
        # player = Advanced("Miro")
        # card = TrapCard("Bombs")
        self.controller.add_player("Advanced", "Miro")
        self.controller.add_card("Trap", "Bombs")
        self.assertEqual(self.controller.add_player_card("Miro", "Bombs"), f"Successfully added card: Bombs to user: Miro")

    def test_add_player_not_success(self):
        self.controller.add_player("Advanced", "Miro")
        self.controller.add_card("Trap", "Bombs")
        self.assertEqual(self.controller.add_player_card("Spiro", "Trap"), None)

    def test_fight_success(self):
        self.controller.add_player("Advanced", "Miro")
        self.controller.add_card("Trap", "Bombs")
        self.controller.add_player("Advanced", "Ivan")
        self.controller.add_card("Magic", "Nuclear")
        self.controller.add_player_card("Miro", "Bombs")
        self.controller.add_player_card("Ivan", "Nuclear")
        msg = f"Attack user health 250 - Enemy user health 210"
        self.assertEqual(self.controller.fight("Miro", "Ivan"), msg)
        # with self.assertRaises(ValueError) as exc:
        # self.assertEqual(str(exc.exception), msg)

    def test_fight_not_success(self):
        self.controller.add_player("Advanced", "Miro")
        self.controller.add_card("Trap", "Bombs")
        self.controller.add_player("Advanced", "Ivan")
        self.controller.add_card("Magic", "Nuclear")
        self.controller.add_player_card("Miro", "Bombs")
        self.assertEqual(self.controller.fight("Miro", "Pesho"), None)

    def test_report(self):
        self.controller.add_player("Advanced", "Miro")
        self.controller.add_player("Advanced", "Ivan")
        self.controller.add_card("Trap", "Bombs")
        self.controller.add_card("Magic", "Nuclear")
        self.controller.add_card("Magic", "Boom")
        self.controller.add_player_card("Miro", "Bombs")
        self.controller.add_player_card("Miro", "Boom")
        self.controller.add_player_card("Ivan", "Nuclear")
        result = f"Username: Miro - Health: 250 - Cards 2" + '\n'
        result += f"### Card: Bombs - Damage: 120" + '\n'
        result += f"### Card: Boom - Damage: 5" + '\n'
        result += f"Username: Ivan - Health: 250 - Cards 1" + '\n'
        result += f"### Card: Nuclear - Damage: 5" + '\n'
        self.assertEqual(self.controller.report(), result)


if __name__ == "__main__":
    unittest.main()
