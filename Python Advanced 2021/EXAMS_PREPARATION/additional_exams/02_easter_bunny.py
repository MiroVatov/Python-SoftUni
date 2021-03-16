def in_range(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def print_directions(best_dir):
    for direction in best_dir:
        print(direction)


size = int(input())
matrix = [[] for _ in range(size)]

BUNNY = 'B'
TRAP = 'X'
MAX_EGGS_SUM = -1_000_000
bunny_starting_row, bunny_starting_col = 0, 0

for row in range(len(matrix)):
    matrix[row] = list(input().split())
    if BUNNY in matrix[row]:
        bunny_starting_row, bunny_starting_col = row, matrix[row].index(BUNNY)

direction = ''
eggs_sum = 0
directions_list = []
best_directions = []

moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for move in moves.items():
    bunny_current_row, bunny_current_col = bunny_starting_row, bunny_starting_col
    bunny_current_row += move[1][0]
    bunny_current_col += move[1][1]
    directions_list = []
    eggs_sum = 0

    while in_range(bunny_current_row, bunny_current_col, size):

        if matrix[bunny_current_row][bunny_current_col] != TRAP:
            eggs_sum += int(matrix[bunny_current_row][bunny_current_col])
            directions_list.append([bunny_current_row, bunny_current_col])
            bunny_current_row += move[1][0]
            bunny_current_col += move[1][1]
        else:
            break

    if eggs_sum > MAX_EGGS_SUM:
        MAX_EGGS_SUM = eggs_sum
        best_directions = directions_list
        direction = move

print(direction[0])
print_directions(best_directions)
print(MAX_EGGS_SUM)
