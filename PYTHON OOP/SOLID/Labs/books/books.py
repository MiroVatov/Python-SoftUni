class Book:
    def __init__(self, author, location):
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f"{self.author}: {self.location}, {self.page}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        if title not in self.books:
            self.books.append(title)

    def find_book(self, title):
        if title in self.books:
            return f"Book {title} found in the Library!"
        return "No such book in the Library"

    def __repr__(self):
        return f"{', '.join([str(book) for book in self.books])}"


b = Book("Tolkien", "Scotland")
b.turn_page(223)
print(b)
b2 = Book("Mordor", "New Zealand")
lib = Library()
print(lib.find_book("Bilbo Begins"))
print(lib.books)
print(lib.add_book(b))
print(lib.add_book(b2))
print(lib)
