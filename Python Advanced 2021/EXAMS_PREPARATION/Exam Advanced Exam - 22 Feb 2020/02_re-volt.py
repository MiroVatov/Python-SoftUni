def create_matrix(n):
    matrix = [[] * n for _ in range(n)]
    for row in range(len(matrix)):
        matrix[row] = list(input())
    return matrix


def starting_position(matrix, player):
    for row in range(len(matrix)):
        if player in matrix[row]:
            return row, matrix[row].index(player)


def valid_move(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def print_matrix(matrix):
    for row in range(len(matrix)):
        print(f"{''.join(map(str, matrix[row]))}")


def change_position(r, c, size):
    if r < 0:
        r = size - 1
    if r >= size:
        r = 0
    if c < 0:
        c = size - 1
    if c >= size:
        c = 0
    return r, c


def move_player(row, col, dir_dict, move_com):
    row += dir_dict[move_com][0]
    col += dir_dict[move_com][1]
    return row, col


size = int(input())
n_commands = int(input())

PLAYER_START = 'f'  # starting position
EMPTY_SLOT = '-'
FINISH = 'F'  #  break
BONUS = 'B'  #  move step forward
TRAP = 'T'  #  move step backward

re_volt_matrix = create_matrix(size)
player_start_position = starting_position(re_volt_matrix, PLAYER_START)
player_current_row, player_current_col = player_start_position[0], player_start_position[1]

directions_dict = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
}

player_won = False

for num in range(n_commands):

    move_command = input()

    player_last_row = player_current_row
    player_last_col = player_current_col

    if move_command == 'up':
        player_current_row, player_current_col = move_player(player_current_row, player_current_col, directions_dict, move_command)

    elif move_command == 'down':
        player_current_row, player_current_col = move_player(player_current_row, player_current_col, directions_dict, move_command)

    elif move_command == 'left':
        player_current_row, player_current_col = move_player(player_current_row, player_current_col, directions_dict, move_command)

    elif move_command == 'right':
        player_current_row, player_current_col = move_player(player_current_row, player_current_col, directions_dict, move_command)

    if not valid_move(player_current_row, player_current_col, size):
        player_current_row, player_current_col = change_position(player_current_row, player_current_col, size)

    if re_volt_matrix[player_current_row][player_current_col] == FINISH:
        player_won = True
        re_volt_matrix[player_last_row][player_last_col] = EMPTY_SLOT
        re_volt_matrix[player_current_row][player_current_col] = PLAYER_START
        break

    elif re_volt_matrix[player_current_row][player_current_col] == BONUS:
        player_current_row, player_current_col = move_player(player_current_row, player_current_col, directions_dict, move_command)
        if re_volt_matrix[player_current_row][player_current_col] == FINISH:
            re_volt_matrix[player_last_row][player_last_col] = EMPTY_SLOT
            re_volt_matrix[player_current_row][player_current_col] = PLAYER_START
            player_won = True
            break

    elif re_volt_matrix[player_current_row][player_current_col] == TRAP:
        player_current_row -= directions_dict[move_command][0]
        player_current_col -= directions_dict[move_command][1]

    if not valid_move(player_current_row, player_current_col, size):
        player_current_row, player_current_col = change_position(player_current_row, player_current_col, size)

    re_volt_matrix[player_last_row][player_last_col] = EMPTY_SLOT
    re_volt_matrix[player_current_row][player_current_col] = PLAYER_START


if player_won:
    print(f"Player won!")
else:
    print(f"Player lost!")

print_matrix(re_volt_matrix)
