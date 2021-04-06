

class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}  # empty dictionary which will keep information regarding the authors (key: str)
        # and the books available for each of the authors (list of strings)

        self.rented_books = {}  # ({usernames: {book names: days left}}).

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return f"We could not find such user to remove!"

        self.user_records.remove(user)
        for user, books in self.rented_books.items():
            del self.rented_books[user.username][books]

    def change_username(self, user_id: int, new_username: str):
        users = [user for user in self.user_records if user.user_id == user_id]

        if not users:
            return f"There is no user with id = {user_id}!"

        username_cannot_be_changed = [user for user in self.user_records if user.user_id == user_id and user.username == new_username]
        if username_cannot_be_changed:
            return f"Please check again the provided username - it should be different than the username used so far!"

        username_can_be_changed = [user for user in self.user_records if user.user_id == user_id and user.username != new_username]
        if username_can_be_changed:
            self.user_records[0].username = new_username

            for user, books in self.rented_books.items():
                if user.user_id == user_id and user.username != new_username:
                    self.rented_books[user.username] = new_username
            return f"Username successfully changed to: {new_username} for userid: {user_id}"


