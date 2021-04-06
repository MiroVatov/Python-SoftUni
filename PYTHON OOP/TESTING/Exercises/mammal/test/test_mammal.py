from mammal.project.mammal import Mammal
import unittest


class MammalTest(unittest.TestCase):

    def setUp(self):
        self.animal = Mammal('Monny', 'Monkey', 'Squiick')

    def test_init(self):
        self.assertEqual(self.animal.name, 'Monny')
        self.assertEqual(self.animal.type, 'Monkey')
        self.assertEqual(self.animal.sound, 'Squiick')

    def test_mammal_kingdom_type(self):
        result = Mammal.get_kingdom(self.animal)
        expected_result = 'animals'
        self.assertEqual(result, expected_result)

    def test_if_get_kingdom_method_is_private(self):
        result = self.animal._Mammal__kingdom
        expected_result = "animals"
        self.assertEqual(result, expected_result)

    def test_make_sound_method(self):
        self.assertEqual(self.animal.make_sound(), 'Monny makes Squiick')

    def test_method_get_kingdom(self):
        self.assertEqual(self.animal.get_kingdom(), 'animals')

    def test_if_info_method_returns_the_correct_result(self):
        self.assertEqual(self.animal.info(), 'Monny is of type Monkey')


if __name__ == "__main__":
    unittest.main()
