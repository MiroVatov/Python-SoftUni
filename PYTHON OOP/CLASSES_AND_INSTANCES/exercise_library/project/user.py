class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        if book_name not in library.books_available[author]:
            days_left = 0
            for user, book in library.rented_books.items():
                for name, days in book.items():
                    if book_name == name:
                        days_left = days
            return f"The book \"{book_name}\" is already rented and will be available in {days_left} days!"

        for book in library.books_available[author]:
            if book == book_name:
                self.books.append(book)
                library.rented_books[self.username] = {book_name: days_to_return}

                # Version 1
                for book in library.books_available[author]:
                    if book == book_name:
                        library.books_available[author].remove(book_name)

                # Version 2
                # library.books_available[author].remove(book_name)

                return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"

        self.books.remove(book_name)
        library.books_available[author].append(book_name)

        # Version 1

        del library.rented_books[self.username][book_name]

        # Version 2

        # for name in library.rented_books.items():
        #     for book in name:
        #         if book == book_name:
        #             del library.rented_books[self.username][book_name]

    def info(self):
        return ', '.join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
