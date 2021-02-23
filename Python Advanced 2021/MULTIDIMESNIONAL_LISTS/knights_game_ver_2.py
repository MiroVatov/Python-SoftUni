def valid_move(pot_rows, pot_cols, size):
    if 0 <= pot_rows < size and 0 <= pot_cols < size:
        return True
    return False


def kills(row, col):
    knight_kills = 0
    knight_moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
    for pos in knight_moves:
        rows_pos, cols_pos = pos
        potential_rows, potential_cols = (row + rows_pos, col + cols_pos)
        if valid_move(potential_rows, potential_cols, size):
            if chess_field[potential_rows][potential_cols] == 'K':
                knight_kills += 1
    return knight_kills


size = int(input())
chess_field = [[] for _ in range(size)]

for chess_row in range(size):
    chess_field[chess_row] = list(input())

max_kills = 0
removed_knights = 0
max_killer_position = 0
can_kill = False

while True:
    knight_kills = 0

    for row in range(size):
        for col in range(size):
            knight_position = chess_field[row][col]
            if knight_position == "K":
                knight_kills = kills(row, col)
                if knight_kills > 0:
                    can_kill = True
                if knight_kills > max_kills:
                    max_kills = knight_kills
                    max_killer_position = (row, col)
                knight_kills = 0

    if not can_kill:
        break
    knight_to_remove_row, knight_to_remove_col = max_killer_position
    chess_field[knight_to_remove_row][knight_to_remove_col] = '0'
    removed_knights += 1
    max_kills = 0
    can_kill = False
    max_killer_position = 0

print(removed_knights)
