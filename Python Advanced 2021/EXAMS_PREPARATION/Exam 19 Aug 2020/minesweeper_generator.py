def bombs_counter(curr_row, curr_col, mine_field, size):
    bomb_moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1),  (0, -1), (-1, -1)]
    bombs_num = 0
    starting_row, starting_col = curr_row, curr_col
    for move in bomb_moves:
        curr_row += move[0]
        curr_col += move[1]
        if 0 <= curr_row < size and 0 <= curr_col < size:
            if mine_field[curr_row][curr_col] == BOMB:
                bombs_num += 1
        curr_row, curr_col = starting_row, starting_col
    return bombs_num


def print_mine_field(field):
    for mine in range(len(field)):
        print(' '.join(map(str, field[mine])))


size = int(input())
number_of_bombs = int(input())

mine_field = [['' for el in range(size)] for _ in range(size)]

BOMB = '*'

for n in range(number_of_bombs):
    raw_input = input().strip('(')
    raw_input = raw_input.strip(')')
    bomb_position = tuple(map(int, raw_input.split(', ')))
    bomb_row, bomb_col = bomb_position[0], bomb_position[1]
    mine_field[bomb_row][bomb_col] = BOMB

for row in range(size):
    for col in range(size):
        if mine_field[row][col] is not BOMB:
            bombs_number = bombs_counter(row, col, mine_field, size)
            mine_field[row][col] = bombs_number

print_mine_field(mine_field)