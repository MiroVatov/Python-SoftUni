finished = False

phones_book = {}
num_names = 0

while not finished:
    contact_info = input()

    # try:
    #     num_names = int(contact_info)
    #     finished = True
    #
    # except ValueError:  # except cannot be used bare -> without error type
    #     name, phone = tuple(contact_info.split('-'))  # Tuple unpacking.
    #     phones_book[name] = phone

    if contact_info.isdigit():
        num_names = int(contact_info)
        finished = True
    else:
        name, phone = tuple(contact_info.split('-'))  # Tuple unpacking, like the list unpacking.
        phones_book[name] = phone

for i in range(num_names):
    name_to_check = input()
    if name_to_check in phones_book:
        print(f'{name_to_check} -> {phones_book[name_to_check]}')
    else:
        print(f'Contact {name_to_check} does not exist.')

