def is_valid(row, col, r1, c1, r2, c2):
    if 0 <= r1 < row and 0 <= c1 < col and 0 <= r2 < row and 0 <= c2 < col:
        return True
    return False


rows, cols = [int(el) for el in input().split()]
matrix = [[e for e in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == 'END':
        break
    if len(command) == 5 and command[0] == 'swap':
        row1 = int(command[1])
        col1 = int(command[2])
        row2 = int(command[3])
        col2 = int(command[4])
        if is_valid(rows, cols, row1, col1, row2, col2):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            print('\n'.join([' '.join(map(str, row)) for row in matrix]))
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')