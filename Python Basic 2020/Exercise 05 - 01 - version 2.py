favourite_book = input()
num_books = 0
fav_book = False

while fav_book != True:
    book = input()
    if book == favourite_book:
        fav_book = True
        print(f'You checked {num_books} books and found it.')
        break
    elif book != 'No More Books':
        num_books += 1
    else:
        print(f'The book you search is not here!')
        print(f'You checked {num_books} books.')
        break
