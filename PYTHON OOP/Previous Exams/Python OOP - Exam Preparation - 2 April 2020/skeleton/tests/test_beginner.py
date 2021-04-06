import unittest

from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):

    def test_successful_create_beginner_player(self):
        self.beginner_player = Beginner("Miron")
        self.assertEqual(self.beginner_player.health, 50)
        self.assertEqual(self.beginner_player.username, "Miron")
        self.assertEqual(self.beginner_player.card_repository, self.beginner_player.card_repository)

    def test_advanced_player__init__with_empty_username_raises_error(self):
        with self.assertRaises(ValueError) as exc:
            self.beginner_player = Beginner("Miro")
            self.beginner_player.username = ''
        msg = "Player's username cannot be an empty string."
        self.assertEqual(str(exc.exception), msg)

    def test_advanced_player__init__with_health_under_zero_raises_error(self):
        with self.assertRaises(ValueError) as exc:
            self.beginner_player = Beginner("Miron")
            self.beginner_player.health = -9
        msg = "Player's health bonus cannot be less than zero."
        self.assertEqual(str(exc.exception), msg)

    def test_is_dead_False(self):
        self.beginner_player = Beginner("Miron")
        self.assertEqual(self.beginner_player.is_dead, False)

    def test_is_dead_True(self):
        self.beginner_player = Beginner("Miron")
        self.beginner_player.health = 0
        self.assertEqual(self.beginner_player.is_dead, True)

    def test_take_damage_method_raises_value_error(self):
        self.beginner_player = Beginner("Miro")
        with self.assertRaises(ValueError) as exc:
            self.beginner_player.take_damage(-2)
        msg = "Damage points cannot be less than zero."
        self.assertEqual(str(exc.exception), msg)

    def test_take_damage_method_health_decreased(self):
        self.beginner_player = Beginner("Miro")
        self.beginner_player.take_damage(30)
        self.assertEqual(self.beginner_player.health, 20)

    def test_if_after_taking_damage_players_health_is_below_zero(self):
        self.beginner_player = Beginner("Miro")
        with self.assertRaises(ValueError) as exc:
            self.beginner_player.take_damage(55)
        msg = "Player's health bonus cannot be less than zero."
        self.assertEqual(str(exc.exception), msg)


if __name__ == "__main__":
    unittest.main()