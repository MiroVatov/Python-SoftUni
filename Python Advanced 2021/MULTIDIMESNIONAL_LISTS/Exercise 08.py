def find_starting_position(field, size):
    pos = []
    for row in field:
        for col in row:
            if col == 's':
                pos.append(field.index(row))
                pos.append(row.index(col))
                return pos


def valid_position(pos, size):
    row, col = pos[0], pos[1]
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


n = int(input())
commands = [e for e in input().split()]

field = [[e for e in input().split()] for _ in range(n)]
starting_position = find_starting_position(field, n)
current_position = starting_position
coals_left = len([e for m in field for e in m if e == 'c'])
game_over = False
position = []

for i in range(len(commands)):

    command = commands[i]
    row = current_position[0]
    col = current_position[1]

    if command == 'up':
        up_move = [-1, 0]
        position = [row + up_move[0], col + up_move[1]]
        if valid_position(position, n):
            current_position = [row + up_move[0], col + up_move[1]]
            row, col = current_position[0], current_position[1]
            if field[row][col] == 'e':
                print(f"Game over! ({row}, {col})")
                game_over = True
                break

            elif field[row][col] == 'c':
                field[row][col] = '*'
                coals_left -= 1
                if coals_left == 0:
                    game_over = True
                    print(f"You collected all coals! ({row}, {col})")
                    break

    elif command == 'down':
        down_move = [1, 0]
        position = [row + down_move[0], col + down_move[1]]
        if valid_position(position, n):
            current_position = [row + down_move[0], col + down_move[1]]
            row, col = current_position[0], current_position[1]
            if field[row][col] == 'e':
                print(f"Game over! ({row}, {col})")
                game_over = True
                break

            elif field[row][col] == 'c':
                field[row][col] = '*'
                coals_left -= 1
                if coals_left == 0:
                    print(f"You collected all coals! ({row}, {col})")
                    game_over = True
                    break

    elif command == 'left':
        left_move = [0, -1]
        position = [row + left_move[0], col + left_move[1]]
        if valid_position(position, n):
            current_position = [row + left_move[0], col + left_move[1]]
            row, col = current_position[0], current_position[1]
            if field[row][col] == 'e':
                print(f"Game over! ({row}, {col})")
                game_over = True
                break

            elif field[row][col] == 'c':
                field[row][col] = '*'
                coals_left -= 1
                if coals_left == 0:
                    print(f"You collected all coals! ({row}, {col})")
                    game_over = True
                    break

    elif command == 'right':
        right_move = [0, 1]
        position = [row + right_move[0], col + right_move[1]]
        if valid_position(position, n):
            current_position = [row + right_move[0], col + right_move[1]]
            row, col = current_position[0], current_position[1]
            if field[row][col] == 'e':
                print(f"Game over! ({row}, {col})")
                game_over = True
                break

            elif field[row][col] == 'c':
                field[row][col] = '*'
                coals_left -= 1
                if coals_left == 0:
                    print(f"You collected all coals! ({row}, {col})")
                    game_over = True
                    break

if not game_over:
    print(f"{coals_left} coals left. ({current_position[0]}, {current_position[1]})")