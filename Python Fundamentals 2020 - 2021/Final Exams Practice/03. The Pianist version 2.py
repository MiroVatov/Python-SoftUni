def piece_checker(piece_dict, piece):
    if piece not in piece_dict:
        return True
    return False


number_of_pieces = int(input())

pieces_dict = {}

for n in range(number_of_pieces):
    piece_info = input().split('|')
    piece_name = piece_info[0]
    composer = piece_info[1]
    piece_key = piece_info[2]

    if piece_name not in pieces_dict:
        pieces_dict[piece_name] = [composer, piece_key]

while True:
    command = input().split('|')
    if command[0] == 'Stop':
        break
    action = command[0]

    if action == 'Add':
        piece_name, composer, piece_key = command[1], command[2], command[3]  # check if the input is not valid (more or less inputs thna the splitted variables) this will bring error
        if piece_checker(pieces_dict, piece_name):                            # split like the normal way with token ....... ->
            pieces_dict[piece_name] = [composer, piece_key]
            print(f"{piece_name} by {composer} in {piece_key} added to the collection!")
        else:
            print(f"{piece_name} is already in the collection!")

    elif action == 'Remove':
        piece_name = command[1]
        if not piece_checker(pieces_dict, piece_name):
            del pieces_dict[piece_name]
            print(f"Successfully removed {piece_name}!")  # check if the deleted piece cannot be displayed
        else:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")

    elif action == 'ChangeKey':
        piece_name, new_key = command[1], command[2]

        if not piece_checker(pieces_dict, piece_name):
            pieces_dict[piece_name][1] = new_key
            print(f'Changed the key of {piece_name} to {new_key}!')
        else:
            print(f'Invalid operation! {piece_name} does not exist in the collection.')

sorted_pieces_dict = dict(sorted(pieces_dict.items(), key=lambda x: (x, x[0])))

for piece, details in sorted_pieces_dict.items():
    print(f"{piece} -> Composer: {details[0]}, Key: {details[1]}")