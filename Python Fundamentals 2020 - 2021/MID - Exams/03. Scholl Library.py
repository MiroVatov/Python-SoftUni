def is_present(books_list, book):
    if book in books_list:
        return True


def swap(books_list, book1, book2):
    if book1 in books_list and book2 in books_list:
        ind_1, ind_2 = books_list.index(book1), books_list.index(book2)
        books_list[ind_1], books_list[ind_2] = books_list[ind_2], books_list[ind_1]
        return books_list


books_shelf = input().split("&")

while True:
    command = input()

    if command == "Done":
        break
    token = command.split(" | ")
    action = token[0]

    if action == "Add Book":
        book_name = token[1]
        if is_present(books_shelf, book_name):
            continue
        else:
            books_shelf.insert(0, book_name)

    elif action == "Take Book":
        book_name = token[1]
        if is_present(books_shelf, book_name):
            books_shelf.remove(book_name)

    elif action == "Swap Books":
        book_name = token[1]
        book_2 = token[2]
        swap(books_shelf, book_name, book_2)

    elif action == "Insert Book":
        book_name = token[1]
        books_shelf.append(book_name)

    elif action == "Check Book":
        index = int(token[1])
        if index in range(len(books_shelf)):
            print(books_shelf[index])

print(f"{', '.join(books_shelf)}")