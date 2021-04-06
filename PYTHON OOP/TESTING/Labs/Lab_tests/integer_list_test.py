import unittest
from integer_list.extended_list import IntegerList


class IntegerListTests(unittest.TestCase):

    def setUp(self):
        self.integer_list = IntegerList([])

    def tearDown(self):
        self.integer_list = None

    def test_add(self):
        self.assertEqual(self.integer_list.add(30), [30])

    def test_add_raises_value_error(self):
        # Variant 1
        # self.assertRaises(ValueError, self.integer_list.add, 'doni')

        # Variant 2, with context manager -> works perfectly fine, both cases

        with self.assertRaises(ValueError):
            self.integer_list.add('doni')

    def test_remove_index(self):
        self.integer_list.add(9)
        self.integer_list.add(11)
        self.integer_list.add(45)
        result = self.integer_list.remove_index(2)
        self.assertEqual(result, 45)

    def test_remove_by_index_raises_index_error(self):
        self.integer_list.add(45)

        # Variant 1 -->>
        # self.assertRaises(IndexError, self.integer_list.remove_index, 5)

        # Variant 2 -->> with context manager

        with self.assertRaises(IndexError):
            self.assertRaises(self.integer_list.remove_index(5))

    def test_init_takes_only_integers(self):
        result = IntegerList('1', 2, 3)
        self.assertEqual(result.get_data(), [2, 3])

    def test_get(self):
        self.integer_list.add(3)
        self.integer_list.add(5)
        result = self.integer_list.get(1)
        self.assertEqual(result, 5)

    def test_get_raises_index_error(self):
        self.assertRaises(IndexError, self.integer_list.get, 0)

    def test_insert_raises_index_error(self):
        self.integer_list.add(3)
        self.integer_list.add(5)
        self.integer_list.add(97)
        self.integer_list.add(15)
        self.assertRaises(IndexError, self.integer_list.insert, 8, 2)

    def test_insert_raises_value_error(self):
        self.integer_list.add(97)
        self.integer_list.add(15)
        self.assertRaises(ValueError, self.integer_list.insert, 1, "9")

    def test_insert_working_properly(self):
        self.integer_list.add(97)
        self.integer_list.add(15)
        self.assertEqual(self.integer_list.insert(1, 9), None)

    def test_get_biggest(self):
        self.integer_list.add(3)
        self.integer_list.add(5)
        self.integer_list.add(97)
        self.integer_list.add(15)
        result = self.integer_list.get_biggest()
        self.assertEqual(result, 97)

    def test_get_index(self):
        self.integer_list.add(5)
        self.integer_list.add(15)
        result = self.integer_list.get_index(5)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()




