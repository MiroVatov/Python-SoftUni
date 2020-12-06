def is_valid_index(length, index):
    return 0 <= index < length


pirateship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
length_warship = len(warship)
length_pirateship = len(pirateship)
maximum_health = int(input())

command_input = input()
stop_game = False

while command_input != 'Retire':
    tokens = command_input.split()
    command = tokens[0]

    if command == 'Fire':
        index = int(tokens[1])
        damage = int(tokens[2])

        if not is_valid_index(length_warship, index):
            command_input = input()
            continue
        warship[index] -= damage

        if warship[index] <= 0:
            print(f'You won! The enemy ship has sunken.')
            stop_game = True
            break
    elif command == 'Defend':
        first_index = int(tokens[1])
        second_index = int(tokens[2])
        damage = int(tokens[3])

        if not (is_valid_index(length_pirateship, first_index) and is_valid_index(length_pirateship, second_index)):
            command_input = input()
            continue

        for i in range(first_index, second_index + 1):
            pirateship[i] -= damage

            if pirateship[i] <= 0:
                print(f'You lost! The pirate ship has sunken.')
                stop_game = True
                break

    elif command == 'Repair':
        index = int(tokens[1])
        health = int(tokens[2])

        if not is_valid_index(length_pirateship, index):
            command_input = input()
            continue
        pirateship[index] += health

        if pirateship[index] > maximum_health:
            pirateship[index] = maximum_health

    elif command == 'Status':
        counter = 0

        for section in pirateship:
            if section < (maximum_health * 0.2):
                counter += 1
        print(f'{counter} sections need repair.')

    command_input = input()

if not stop_game:
    print(f'Pirate ship status: {sum(pirateship)}')
    print(f'Warship status: {sum(warship)}')









