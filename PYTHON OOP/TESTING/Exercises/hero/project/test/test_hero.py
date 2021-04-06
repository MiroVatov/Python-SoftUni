import unittest
from hero.project.project.hero import Hero


def check_if_both_names_are_the_same(hero_name, enemy_name):
    if hero_name == enemy_name:
        return True
    return False


class HeroTest(unittest.TestCase):

    # def setUp(self):
    #     self.hero = Hero('Miro', 100, 850, 5)  # username: Miro, level: 100, health: 150, damage: 25
    #     self.enemy_hero = Hero('Prodigy', 90, 830, 5)  # username: Prodigy, level: 90, health: 130, damage: 25

    def test_both_enemies_fight_with_the_same_name_raises_exception(self):
        self.hero = Hero('Miro', 100, 850, 5)
        self.enemy_hero = Hero('Prodigy', 90, 830, 5)
        self.enemy_hero.username = self.hero.username

        if check_if_both_names_are_the_same(self.hero.username, self.enemy_hero.username):
            with self.assertRaises(Exception):
                Hero.battle(self.hero, self.enemy_hero)

    def test_hero_health_is_zero_or_below_zero_raises_exception(self):
        self.hero = Hero('Miro', 100, 850, 5)
        self.enemy_hero = Hero('Prodigy', 90, 830, 5)
        self.hero.health = 0
        with self.assertRaises(ValueError):
            Hero.battle(self.hero, self.enemy_hero)

    def test_enemy_hero_health_is_zero_or_below_zero_raises_exception(self):
        self.hero = Hero('Miro', 100, 850, 5)
        self.enemy_hero = Hero('Prodigy', 90, 830, 5)
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError):
            Hero.battle(self.hero, self.enemy_hero)

    def test_if_both_enemies_health_is_zero_or_blow_zero(self):
        self.hero = Hero('Miro', 100, 350, 5)
        self.enemy_hero = Hero('Prodigy', 90, 330, 5)
        result = Hero.battle(self.hero, self.enemy_hero)
        self.assertEqual(result, 'Draw')

    def test_if_enemy_hero_health_drops_to_zero_or_under_zero(self):
        self.hero = Hero('Miro', 100, 850, 5)
        self.enemy_hero = Hero('Prodigy', 90, 330, 5)
        result = Hero.battle(self.hero, self.enemy_hero)
        self.assertEqual(self.hero.level, 101)
        self.assertEqual(self.hero.health, 405)
        self.assertEqual(self.hero.damage, 10)
        self.assertEqual(result, 'You win')

    def test_if_enemy_health_is_above_zero_after_battle_nd_hero_loses_the_battle(self):
        self.hero = Hero('Miro', 100, 850, 5)
        self.enemy_hero = Hero('Prodigy', 90, 830, 5)
        result = Hero.battle(self.hero, self.enemy_hero)
        self.assertEqual(self.enemy_hero.level, 91)
        self.assertEqual(self.enemy_hero.health, 335)
        self.assertEqual(self.enemy_hero.damage, 10)
        self.assertEqual(result, "You lose")

    def test_string_method_prints_the_expected_string(self):
        self.hero = Hero('Miro', 100, 850, 5)

        result = Hero.__str__(self.hero)
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                          f"Health: {self.hero.health}\n" \
                          f"Damage: {self.hero.damage}\n"
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

