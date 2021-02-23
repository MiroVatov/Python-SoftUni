def is_move_valid(next_row, next_col, rows, cols):
    if 0 <= next_row < rows and 0 <= next_col < cols:
        return True
    return False


def print_matrix(playing_filed):
    for el in playing_filed:
        print(''.join(el))


rows, cols = [int(e) for e in input().split()]

playing_field = [[] * rows for _ in range(rows)]

BUNNY = 'B'
PLAYER = 'P'
FREE_SPACE = '.'
LEFT = 'L'
RIGHT = 'R'
UP = 'U'
DOWN = 'D'

player_current_row = 0
player_current_col = 0

for row in range(len(playing_field)):
    playing_field[row] = list(input())
    if PLAYER in playing_field[row]:
        player_current_row, player_current_col = row, playing_field[row].index(PLAYER)


moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

commands = list(input())

is_won = False
is_dead = False
player_next_row, player_next_col = player_current_row, player_current_col

player_final_row = 0
player_final_col = 0

for command in commands:
    if is_won or is_dead:
        break
    player_last_row, player_last_col = player_current_row, player_current_col

    player_next_row += moves[command][0]
    player_next_col += moves[command][1]

    if not is_move_valid(player_next_row, player_next_col, rows, cols):
        playing_field[player_last_row][player_last_col] = FREE_SPACE
        player_current_row, player_current_col = player_last_row, player_last_col
        player_final_row, player_final_col = player_current_row, player_current_col
        is_won = True

    elif is_move_valid(player_next_row, player_next_col, rows, cols):
        player_current_row, player_current_col = player_next_row, player_next_col

        if playing_field[player_current_row][player_current_col] == BUNNY:
            player_final_row, player_final_col = player_current_row, player_current_col
            is_dead = True
        else:
            playing_field[player_last_row][player_last_col] = FREE_SPACE
            playing_field[player_current_row][player_current_col] = PLAYER

    rabbits_positions = []

    for row in range(len(playing_field)):
        for col in range(len(playing_field[row])):
            if playing_field[row][col] == BUNNY:
                rabbits_positions.append((row, col))

    rabbit_position_row = 0
    rabbit_position_col = 0

    for position in rabbits_positions:
        rabbit_position_row = position[0]
        rabbit_position_col = position[1]

        for move in moves:
            rabbit_next_row, rabbit_next_col = rabbit_position_row, rabbit_position_col
            rabbit_next_row += moves[move][0]
            rabbit_next_col += moves[move][1]

            if is_move_valid(rabbit_next_row, rabbit_next_col, rows, cols):
                if playing_field[rabbit_next_row][rabbit_next_col] == PLAYER:
                    player_final_row, player_final_col = player_next_row, player_next_col
                    playing_field[rabbit_next_row][rabbit_next_col] = BUNNY
                    is_dead = True
                else:
                    playing_field[rabbit_next_row][rabbit_next_col] = BUNNY


print_matrix(playing_field)

if is_won and not is_dead:
    print(f"won: {player_final_row} {player_final_col}")
else:
    print(f"dead: {player_final_row} {player_final_col}")