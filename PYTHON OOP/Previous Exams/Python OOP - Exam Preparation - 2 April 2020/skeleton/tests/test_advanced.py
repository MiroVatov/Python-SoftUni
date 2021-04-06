import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):

    def test_successful_create_advanced_player(self):
        self.advanced_player = Advanced("Miron")
        self.assertEqual(self.advanced_player.health, 250)
        self.assertEqual(self.advanced_player.username, "Miron")
        self.assertEqual(self.advanced_player.card_repository, self.advanced_player.card_repository)

    def test_advanced_player__init__with_empty_username_raises_error(self):
        with self.assertRaises(ValueError) as exc:
            self.advanced_player = Advanced("Miro")
            self.advanced_player.username = ''
        msg = "Player's username cannot be an empty string."
        self.assertEqual(str(exc.exception), msg)

    def test_advanced_player__init__with_health_under_zero_raises_error(self):
        with self.assertRaises(ValueError) as exc:
            self.advanced_player = Advanced("Miron")
            self.advanced_player.health = -9
        msg = "Player's health bonus cannot be less than zero."
        self.assertEqual(str(exc.exception), msg)

    def test_is_dead_False(self):
        self.advanced_player = Advanced("Miron")
        self.assertEqual(self.advanced_player.is_dead, False)

    def test_is_dead_True(self):
        self.advanced_player = Advanced("Miron")
        self.advanced_player.health = 0
        self.assertEqual(self.advanced_player.is_dead, True)

    def test_take_damage_method_raises_value_error(self):
        self.advanced_player = Advanced("Miro")
        with self.assertRaises(ValueError) as exc:
            self.advanced_player.take_damage(-2)
        msg = "Damage points cannot be less than zero."
        self.assertEqual(str(exc.exception), msg)

    def test_take_damage_method_health_decreased(self):
        self.advanced_player = Advanced("Miro")
        self.advanced_player.take_damage(30)
        self.assertEqual(self.advanced_player.health, 220)

    def test_if_after_taking_damage_players_health_is_below_zero(self):
        self.advanced_player = Advanced("Miro")
        with self.assertRaises(ValueError) as exc:
            self.advanced_player.take_damage(255)
        msg = "Player's health bonus cannot be less than zero."
        self.assertEqual(str(exc.exception), msg)


if __name__ == "__main__":
    unittest.main()
