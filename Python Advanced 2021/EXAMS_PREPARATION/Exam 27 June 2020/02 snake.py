field_size = int(input())
snake_field = [list(input()) for _ in range(field_size)]


def check_starting_position(field, start):
    for row in range(len(field)):
        if start in field[row]:
            return row, field[row].index(start)


def is_outside(cur_row, cur_col, size):
    if 0 <= cur_row < size and 0 <= cur_col < size:
        return False
    return True


def find_burrow(field, burrow):
    burrows = 0
    for row in range(len(field)):
        if burrow in field[row]:
            burrows += 1
            if burrows == 2:
                return row, field[row].index(burrow)


def print_snake_filed(field):
    for row in range(len(field)):
        print(''.join(field[row]))


START = 'S'
BURROW = 'B'

# 'S' -> snake starting position
# '*' -> food
# 'B' -> burrow must be 2 with B's
# '-' -> empty positions
# '.' -> snake trails

food_qty = 0

starting_row, starting_col = check_starting_position(snake_field, START)

current_row, current_col = starting_row, starting_col

move_commands = ["up", "down", "left", "right"]

UP_MOVE = (-1, 0)
DOWN_MOVE = (1, 0)
LEFT_MOVE = (0, -1)
RIGHT_MOVE = (0, 1)

while food_qty < 10:
    direction = input()

    last_row, last_col = current_row, current_col
    if direction in move_commands:
        if direction == 'up':
            current_row += UP_MOVE[0]
            current_col += UP_MOVE[1]

        elif direction == 'down':
            current_row += DOWN_MOVE[0]
            current_col += DOWN_MOVE[1]

        elif direction == 'left':
            current_row += LEFT_MOVE[0]
            current_col += LEFT_MOVE[1]

        elif direction == 'right':
            current_row += RIGHT_MOVE[0]
            current_col += RIGHT_MOVE[1]

        if is_outside(current_row, current_col, field_size):
            snake_field[last_row][last_col] = '.'
            print("Game over!")
            break

        if snake_field[current_row][current_col] == '*':
            food_qty += 1
            snake_field[last_row][last_col] = '.'
            snake_field[current_row][current_col] = 'S'

        elif snake_field[current_row][current_col] == '-':
            snake_field[last_row][last_col] = '.'
            snake_field[current_row][current_col] = 'S'

        elif snake_field[current_row][current_col] == 'B':
            burrow_end_position = find_burrow(snake_field, BURROW)
            snake_field[last_row][last_col] = '.'
            snake_field[current_row][current_col] = '.'
            current_row, current_col = burrow_end_position[0], burrow_end_position[1]
            snake_field[current_row][current_col] = 'S'

if food_qty >= 10:
    print(f"You won! You fed the snake.")

print(f"Food eaten: {food_qty}")
print_snake_filed(snake_field)