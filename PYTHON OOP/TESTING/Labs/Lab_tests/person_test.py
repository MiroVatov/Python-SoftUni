import unittest
from demo_1.solution import Person


class PersonTests(unittest.TestCase):
    def setUp(self):
        self.person = Person('Miro', 'Vatov', 38)

    def test_person_is_properly_initiated(self):
        self.assertEqual(self.person.first_name, "Miro")
        self.assertEqual(self.person.last_name, 'Vatov')
        self.assertEqual(self.person.age, 38)

    def test_is_method_get_full_name_correctly_responding(self):
        full_name = self.person.get_full_name()
        self.assertEqual(full_name, 'Miro Vato')


if __name__ == '__main__':
    unittest.main()
