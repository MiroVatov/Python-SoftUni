number_of_pieces = int(input())

pieces_dict = {}

for n in range(number_of_pieces):
    piece_info = input().split('|')
    piece_name = piece_info[0]
    composer = piece_info[1]
    piece_key = piece_info[2]

    if piece_name not in pieces_dict:
        pieces_dict[piece_name] = {'composer': composer, 'piece_key': piece_key}

while True:
    command = input().split('|')
    if command[0] == 'Stop':
        break
    action = command[0]
    if action == 'Add':
        piece_name = command[1]
        composer = command[2]
        piece_key = command[3]
        if piece_name not in pieces_dict:
            pieces_dict[piece_name] = {'composer': composer, 'piece_key': piece_key}
            print(f"{piece_name} by {composer} in {piece_key} added to the collection!")
        else:
            print(f"{piece_name} is already in the collection!")

    elif action == 'Remove':
        piece_name = command[1]
        if piece_name in pieces_dict:
            del pieces_dict[piece_name]
            print(f"Successfully removed {piece_name}!") # check if the deleted piece cannot be displayed
        else:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")

    elif action == 'ChangeKey':
        piece_name = command[1]
        new_key = command[2]
        if piece_name in pieces_dict:
            pieces_dict[piece_name]['piece_key'] = new_key
            print(f'Changed the key of {piece_name} to {new_key}!')
        else:
            print(f'Invalid operation! {piece_name} does not exist in the collection.')

sorted_pieces_dict = dict(sorted(pieces_dict.items(), key=lambda x: (x, x[0])))

for piece, details in sorted_pieces_dict.items():
    print(f"{piece} -> Composer: {details['composer']}, Key: {details['piece_key']}")