class Person:
    def __init__(self, name):
        self.name = name


class Reader(Person):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def turn_page(book):
        book.pages -= 10
        return book


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"{self.author}: {self.title}, {self.pages}"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book, location):
        if book not in self.books:
            self.books[book.author] = [book.title, book.pages, location]
            return f"Successfully added {book} to the Library!"

    def find_book(self, book: Book):
        if book.author in self.books.keys():
            return f"Book {book.title} from writer {book.author} found in the Library!"
        return "No such book in the Library"

    def print_data(self):
        print([f"{book_name} {location}" for book_name, location in self.books.items()])


b = Book("Bilbo Begins", "Tolkien", 300)
r = Reader("Mircho")
r.turn_page(b)
print(b)
b2 = Book("Mordor", "Jeffry Rush", 500)
lib = Library()
print(lib.books)
print(lib.add_book(b, "Amazon"))
print(lib.add_book(b2, "AliExpress"))
print(lib.find_book(b2))
lib.print_data()
