def nice_kids_count(matrix, NICE_KID_HOUSE):
    nice_kids = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == NICE_KID_HOUSE:
                nice_kids += 1

    return nice_kids


def santa_starting_position(matrix, santa):
    for row in range(len(matrix)):
        if santa in matrix[row]:
            return row, matrix[row].index(santa)


def check_indices(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def move_player(row, col, dir_dict, move_com):
    row += dir_dict[move_com][0]
    col += dir_dict[move_com][1]
    return row, col


def print_matrix(matrix):
    for line in range(len(matrix)):
        print(f"{' '.join(matrix[line])}")


def change_matrix_after_move(matrix, pr_row, pr_col, cur_row, cur_col):
    matrix[pr_row][pr_col] = EMPTY_POSITION
    matrix[cur_row][cur_col] = SANTA
    return matrix


number_of_presents = int(input())
size = int(input())
neighborhood = [list(input().split()) for _ in range(size)]

SANTA = 'S'  # -> Santa's starting position - > Santa moves  - > EMPTY_POSITION
NAUGHTY_KID_HOUSE = 'X'  # don't receive a present in normal cases -> house becomes EMPTY_POSITION
NICE_KID_HOUSE = 'V'  # receives a present always -> house becomes EMPTY_POSITION
EMPTY_POSITION = '-'
COOKIE = 'C'  # -> Santa eats cookies and becomes happy and extra generous to all the kids around him* (meaning all of them will receive presents (doesn’t matter if naughty or nice))
            # But Santa doesn't change his position -> only change the houses to EMPTY_POSITIONS

directions_dict = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
}

#  Keep in mind that you have to check whether all of the nice kids received presents!

santa_current_row, santa_current_col = santa_starting_position(neighborhood, SANTA)

nice_kids_presents = 0

while number_of_presents > 0:
    command = input()
    if command == "Christmas morning":
        break
    santa_previous_row, santa_previous_col = santa_current_row, santa_current_col

    if command == 'up':
        santa_current_row, santa_current_col = move_player(santa_current_row, santa_current_col, directions_dict, command)
    elif command == 'down':
        santa_current_row, santa_current_col = move_player(santa_current_row, santa_current_col, directions_dict, command)
    elif command == 'left':
        santa_current_row, santa_current_col = move_player(santa_current_row, santa_current_col, directions_dict, command)
    elif command == 'right':
        santa_current_row, santa_current_col = move_player(santa_current_row, santa_current_col, directions_dict, command)

    if not check_indices(santa_current_row, santa_current_col, size):
        continue

    if neighborhood[santa_current_row][santa_current_col] == NICE_KID_HOUSE:
        neighborhood = change_matrix_after_move(neighborhood, santa_previous_row, santa_previous_col, santa_current_row, santa_current_col)
        number_of_presents -= 1
        nice_kids_presents += 1

    elif neighborhood[santa_current_row][santa_current_col] == NAUGHTY_KID_HOUSE:
        neighborhood = change_matrix_after_move(neighborhood, santa_previous_row, santa_previous_col, santa_current_row, santa_current_col)

    elif neighborhood[santa_current_row][santa_current_col] == COOKIE:
        neighborhood = change_matrix_after_move(neighborhood, santa_previous_row, santa_previous_col, santa_current_row, santa_current_col)

        for move in directions_dict.values():
            if number_of_presents > 0:
                row = santa_current_row + move[0]
                col = santa_current_col + move[1]
                if neighborhood[row][col] == NICE_KID_HOUSE:
                    neighborhood[row][col] = EMPTY_POSITION
                    number_of_presents -= 1
                    nice_kids_presents += 1

                elif neighborhood[row][col] == NAUGHTY_KID_HOUSE:
                    neighborhood[row][col] = EMPTY_POSITION
                    number_of_presents -= 1

    elif neighborhood[santa_current_row][santa_current_col] == EMPTY_POSITION:
        neighborhood = change_matrix_after_move(neighborhood, santa_previous_row, santa_previous_col, santa_current_row,santa_current_col)

nice_kids = nice_kids_count(neighborhood, NICE_KID_HOUSE)

if number_of_presents <= 0 < nice_kids:
    print(f"Santa ran out of presents!")

print_matrix(neighborhood)

if nice_kids <= 0:
    print(f"Good job, Santa! {nice_kids_presents} happy nice kid/s.")

else:
    print(f"No presents for {nice_kids} nice kid/s.")