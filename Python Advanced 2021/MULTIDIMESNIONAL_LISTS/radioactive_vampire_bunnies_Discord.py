def read_matrix(is_tet=False):
    (rows_count, columns_count) = map(int, input().split())
    matrix = []
    for row_index in range(rows_count):
        row = []
        for ch in input():
            row.append(ch)
        matrix.append(row)
    return matrix


def get_player_coordinates(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 'P':
                player_row = r
                player_col = c
                break
    return (player_row, player_col)


def get_bunnies_coordinates(matrix):
    bunnies_coordinates = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 'B':
                coordinates = (r, c)
                bunnies_coordinates.append(coordinates)
    return bunnies_coordinates


def get_player_moves(matrix, moves, player_row, player_col, player_status):
    for i in range(len(moves)):
        command = moves[i]
        if player_status != 'dead' and player_status != 'win':
            matrix[player_row][player_col] = '.'
        else:
            break
        # Up command
        if command == 'U':
            if player_row - 1 in range(len(matrix)):
                player_row -= 1
            else:
                player_status = 'win'
        # Down command
        elif command == 'D':
            if player_row + 1 in range(len(matrix)):
                player_row += 1
            else:
                player_status = 'win'
        # Left command
        elif command == 'L':
            if player_col - 1 in range(len(matrix[0])):
                player_col -= 1
            else:
                player_status = 'win'
        # Right command
        elif command == 'R':
            if player_col + 1 in range(len(matrix[0])):
                player_col += 1
            else:
                player_status = 'win'
        # Check if the player moved to coordinate with bunnies
        if player_status == 'win':
            matrix[player_row][player_col] = '.'
        elif matrix[player_row][player_col] == 'B':
            player_status = 'dead'
        else:
            matrix[player_row][player_col] = 'P'

        matrix, player_status = get_bunnies_spread(matrix, player_status)

    return matrix, player_status, player_row, player_col


def get_bunnies_spread(matrix, player_status):
    bunnies_coordinates = get_bunnies_coordinates(matrix)
    for curr_coordinates in bunnies_coordinates:
        bunny_row = curr_coordinates[0]
        bunny_col = curr_coordinates[1]
        up_bunny_row = bunny_row - 1
        down_bunny_row = bunny_row + 1
        left_bunny_col = bunny_col - 1
        right_bunny_col = bunny_col + 1
        # Up bunnies extend
        if up_bunny_row in range(len(matrix)):
            if matrix[up_bunny_row][bunny_col] == 'P':
                player_status = 'dead'
            matrix[up_bunny_row][bunny_col] = 'B'
        # Down bunnies extend
        if down_bunny_row in range(len(matrix)):
            if matrix[down_bunny_row][bunny_col] == 'P':
                player_status = 'dead'
            matrix[down_bunny_row][bunny_col] = 'B'
        # Left bunnies extend
        if left_bunny_col in range(len(matrix[0])):
            if matrix[bunny_row][left_bunny_col] == 'P':
                player_status = 'dead'
            matrix[bunny_row][left_bunny_col] = 'B'
        # Right bunnies extend
        if right_bunny_col in range(len(matrix[0])):
            if matrix[bunny_row][right_bunny_col] == 'P':
                player_status = 'dead'
            matrix[bunny_row][right_bunny_col] = 'B'
    return (matrix, player_status)


def print_result(matrix, player_status, player_row, player_col):
    for r in range(len(matrix)):
        row = []
        for c in range(len(matrix[0])):
            row.append(matrix[r][c])
        print(''.join(s for s in row))
    if player_status == 'win':
        print(f'won: {player_row} {player_col}')
    elif player_status == 'dead':
        print(f'dead: {player_row} {player_col}')


matrix = read_matrix()
moves = [s for s in input()]
player_status = ''
player_row, player_col = get_player_coordinates(matrix)
matrix, player_status, player_row, player_col = get_player_moves(matrix, moves, player_row, player_col, player_status)
print_result(matrix, player_status, player_row, player_col)