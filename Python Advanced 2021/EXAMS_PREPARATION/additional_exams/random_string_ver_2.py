def matrix_input() -> [[int]]:
    size = int(input())
    return [[n for n in input()] for _ in range(size)]


def position(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'P':
                return row, col


def is_letter(element):
    if element.isalpha():
        return element


def print_matrix(matrix):
    for row in range(len(matrix)):
        print("".join(matrix[row]))


# TODO - INPUT and CONSTANTS:
initial_string = list(map(str, input()))
matrix = matrix_input()
commands_count = int(input())
RANGE_SQ_MATRIX = [el for el in range(len(matrix))]

for command in range(commands_count):
    action = input()
    row, column = list(position(matrix))

    if action == 'up' and row - 1 in RANGE_SQ_MATRIX:
        letter_to_add = is_letter(matrix[row - 1][column])
        if letter_to_add:
            initial_string.append(letter_to_add)
        matrix[row][column] = "-"
        matrix[row - 1][column] = 'P'

    elif action == 'down' and row + 1 in RANGE_SQ_MATRIX:
        letter_to_add = is_letter(matrix[row + 1][column])
        if letter_to_add:
            initial_string.append(letter_to_add)
        matrix[row][column] = "-"
        matrix[row + 1][column] = 'P'

    elif action == 'left' and column - 1 in RANGE_SQ_MATRIX:
        letter_to_add = is_letter(matrix[row][column - 1])
        if letter_to_add:
            initial_string.append(letter_to_add)
        matrix[row][column] = "-"
        matrix[row][column - 1] = 'P'

    elif action == 'right' and column + 1 in RANGE_SQ_MATRIX:
        letter_to_add = is_letter(matrix[row][column + 1])
        if letter_to_add:
            initial_string.append(letter_to_add)
        matrix[row][column] = "-"
        matrix[row][column + 1] = 'P'

    else:
        if initial_string:
            initial_string.pop()

print("".join(initial_string))
print_matrix(matrix)