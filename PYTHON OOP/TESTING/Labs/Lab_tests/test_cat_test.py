import unittest
from test_cat.test_cat import Cat


class CatTest(unittest.TestCase):

    def setUp(self):
        self.cat = Cat('Benny')

    def tearDown(self):
        self.cat = None

    def test_if_the_cat_size_increased_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_is_cat_fed_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.fed, True)

    def test_cat_cannot_eat_after_is_already_fed(self):
        self.cat.fed = True
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_cannot_fall_asleep_if_not_fed(self):
        self.cat.fed = False
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertEqual(self.cat.sleepy, False)


if __name__ == "__main__":
    unittest.main()
