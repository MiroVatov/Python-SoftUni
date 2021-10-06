import unittest

from project.library import Library


class TestLibrary(unittest.TestCase):

    def test__init__(self):
        self.library = Library("Alex")
        self.assertEqual(self.library.name, "Alex")
        self.assertEqual(self.library.books_by_authors, {})
        self.assertEqual(self.library.readers, {})

    def test__init__name_empty_string(self):
        with self.assertRaises(ValueError) as err:
            self.library = Library("")

        msg = "Name cannot be empty string!"
        self.assertEqual(str(err.exception), msg)

    def test_method_add_book_happy_case(self):
        self.library = Library("Alex")
        self.library.add_book("King", "It")
        self.assertEqual(self.library.books_by_authors["King"], ["It"])

    def test_method_add_book_author_already_in_books_by_author(self):
        self.library = Library("Alex")
        self.library.add_book("King", "It")
        self.library.add_book("King", "Shining")
        self.assertEqual(self.library.books_by_authors["King"], ["It", "Shining"])

    def test_add_book_method_books_already_in_books_by_authors(self):
        self.library = Library("Alex")
        self.library.add_book("King", "It")
        self.library.add_book("King", "It")
        self.library.add_book("Jones", "It")
        self.assertEqual(self.library.books_by_authors["King"], ["It"])
        self.assertEqual(self.library.books_by_authors["Jones"], ["It"])

    def test_method_add_reader_happy_case(self):
        self.library = Library("Alex")
        self.library.add_reader("Miro")
        self.assertEqual(self.library.readers, {"Miro": []})

    def test_method_add_reader_username_already_registered(self):
        self.library = Library("Alex")
        self.library.add_reader("Miro")
        self.assertEqual(self.library.add_reader("Miro"), "Miro is already registered in the Alex library.")

    def test_method_rent_book_happy_case(self):
        self.library = Library("Alex")
        self.library.add_reader("Miro")
        self.library.add_book("King", "It")
        # book_index = self.library.books_by_authors["King"].index("It")
        self.library.rent_book("Miro", "King", "It")
        self.assertEqual(self.library.readers, {"Miro": [{"King": "It"}]})
        self.assertEqual(self.library.books_by_authors, {"King": []})

    def test_method_rent_book_reader_not_in_readers(self):
        self.library = Library("Alex")
        self.assertEqual(self.library.rent_book("Miro", "King", "It"), "Miro is not registered in the Alex Library.")

    def test_method_rent_book_author_not_in_books_by_author(self):
        self.library = Library("Alex")
        self.library.add_reader("Miro")
        self.assertEqual(self.library.rent_book("Miro", "King", "It"), "Alex Library does not have any King's books.")

    def test_method_rent_book_book_title_not_in_books_by_author(self):
        self.library = Library("Alex")
        self.library.add_reader("Miro")
        self.library.add_book("King", "It")
        self.assertEqual(self.library.rent_book("Miro", "King", "Shining"), """Alex Library does not have King's "Shining".""")


if __name__ == "__main__":
    unittest.main()
