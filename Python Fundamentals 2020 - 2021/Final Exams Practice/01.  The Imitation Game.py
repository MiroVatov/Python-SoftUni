def move(message, num):
    part_to_move = message[:num]
    message = message + part_to_move
    message = message.replace(part_to_move, '', 1)
    return message


def insert(message, idx, val):
    message = list(message)
    message.insert(idx, val)
    return ''.join(message)


encrypted_message = input()

while True:
    command = input().split("|")
    action = command[0]
    if action == 'Decode':
        break

    if action == "Move":
        n_letters = int(command[1])
        encrypted_message = move(encrypted_message, n_letters)

    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = insert(encrypted_message, index, value)

    elif action == "ChangeAll":
        subst = command[1]
        replace = command[2]
        encrypted_message = encrypted_message.replace(subst, replace)

print(f"The decrypted message is: {encrypted_message}")