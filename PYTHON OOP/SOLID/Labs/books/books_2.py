class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f"{self.author}: {self.title}, {self.page}"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, location):
        if location not in self.books:
            self.books[title.author] = [title.title, title.page, location]
            return f"Successfully added {title} to the Library!"

    def find_book(self, book: Book):
        if book.author in self.books.keys():
            return f"Book {book.title} from writer {book.author} found in the Library!"
        return "No such book in the Library"

    def __repr__(self):
        data = ''
        for book_name, location in self.books.items():
            data += f"{book_name} : {location}" + '\n'
        return data


b = Book("Bilbo Begins", "Tolkien")
b.turn_page(223)
print(b)
b2 = Book("Mordor", "Jeffry Rush")
lib = Library()
print(lib.books)
print(lib.add_book(b, "Amazon"))
print(lib.add_book(b2, "AliExpress"))
print(lib.find_book(b2))
print(lib)
