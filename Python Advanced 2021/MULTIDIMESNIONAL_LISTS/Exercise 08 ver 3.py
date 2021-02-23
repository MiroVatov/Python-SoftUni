def find_starting_position(field, size):
    pos = []
    for row in field:
        for col in row:
            if col == 's':
                pos.append(field.index(row))
                pos.append(row.index(col))
                return pos


n = int(input())
commands = [e for e in input().split()]

field = [[e for e in input().split()] for _ in range(n)]
starting_position = find_starting_position(field, n)
current_position = starting_position
coals_left = len([e for m in field for e in m if e == 'c'])
game_over = False
next_position = []

for i in range(len(commands)):

    command = commands[i]
    row = current_position[0]
    col = current_position[1]

    if command == 'up':
        move = [-1, 0]
        next_position = [row + move[0], col + move[1]]

    elif command == 'down':
        move = [1, 0]
        next_position = [row + move[0], col + move[1]]

    elif command == 'left':
        move = [0, -1]
        next_position = [row + move[0], col + move[1]]

    elif command == 'right':
        move = [0, 1]
        next_position = [row + move[0], col + move[1]]

    if 0 <= next_position[0] < len(field) and 0 <= next_position[1] < len(field):
        current_position = next_position
        row, col = current_position[0], current_position[1]
        if field[row][col] == 'e':
            print(f"Game over! ({row}, {col})")
            game_over = True
            break

        elif field[row][col] == 'c':
            coals_left -= 1
            if coals_left == 0:
                print(f"You collected all coals! ({row}, {col})")
                game_over = True
                break
            field[row][col] = '*'

if not game_over:
    print(f"{coals_left} coals left. ({current_position[0]}, {current_position[1]})")