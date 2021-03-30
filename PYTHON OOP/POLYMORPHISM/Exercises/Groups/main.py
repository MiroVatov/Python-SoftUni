from groups import Group, Person

import unittest


class TestGroups(unittest.TestCase):
    def setUp(self):
        self.p0 = Person('Aliko', 'Dangote')
        self.p1 = Person('Bill', 'Gates')
        self.p2 = Person('Warren', 'Buffet')
        self.p3 = Person('Elon', 'Musk')

    def test_person_init(self):
        self.assertEqual(self.p0.name, 'Aliko')
        self.assertEqual(self.p0.surname, 'Dangote')

    def test_person_str(self):
        self.assertEqual(str(self.p1), 'Bill Gates')

    def test_person_add(self):
        self.assertEqual(str(self.p2 + self.p3), 'Warren Musk')

    def test_group_init(self):
        first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
        self.assertEqual(first_group.name, '__VIP__')
        self.assertEqual(first_group.people, [self.p0, self.p1, self.p2])

    def test_group_str(self):
        first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
        self.assertEqual(str(first_group), "Group __VIP__ with members Aliko Dangote, Bill Gates, Warren Buffet")

    def test_group_len(self):
        first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
        self.assertEqual(len(first_group), 3)


if __name__ == "__main__":
    unittest.main()

