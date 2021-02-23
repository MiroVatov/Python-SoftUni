def valid_index(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def bomb_explosion(matrix, bomb, size):
    row = bomb[0]
    col = bomb[1]
    bomb_damage = matrix[row][col]
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if valid_index(r, c, size) and matrix[r][c] > 0:
                matrix[r][c] -= bomb_damage
    matrix[row][col] = 0
    return matrix


n = int(input())

matrix = [[int(e) for e in input().split()] for _ in range(n)]

bombs_num = input().split()
bombs = []

for el in bombs_num:
    token = el.split(',')
    f_ind = int(token[0])
    s_ind = int(token[1])
    bombs.append([f_ind, s_ind])

for bomb in bombs:
    damage = matrix[bomb[0]][bomb[1]]
    if damage > 0:
        matrix = bomb_explosion(matrix, bomb, n)

survived_cells = []

for row in matrix:
    for val in row:
        if val > 0:
            survived_cells.append(val)

print(f"Alive cells: {len(survived_cells)}")
print(f"Sum: {sum(survived_cells)}")
print('\n'.join([' '.join(map(str, row)) for row in matrix]))