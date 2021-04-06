from dictionary_iterator import dictionary_iter

import unittest


class DictionaryIteratorTests(unittest.TestCase):
    def test_zero(self):
        result = dictionary_iter({1: "1", 2: "2"})
        expected = []
        for x in result:
            expected.append(x)
        self.assertEqual(expected, [(1, "1"), (2, "2")])


if __name__ == '__main__':
    unittest.main()