WIN_LIMIT_CONDITION = 4
DEFAULT_ROWS_COUNT = 6
DEFAULT_COLUMNS_COUNT = 7


def create_play_board():
    board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
            ]
    return board


def winning_condition(board, row, col, limit, player, rows_count, cols_count):
    if check_horizontal_win(board, limit, player):
        return True
    elif check_vertical_win(board, limit, player):
        return True
    elif check_down_left_diagonal_win(board, row, col, limit, player, rows_count, cols_count):
        return True
    elif check_down_right_diagonal_win(board, row, col, limit, player, rows_count, cols_count):
        return True
    elif check_up_left_diagonal_win(board, row, col, limit, player, rows_count, cols_count):
        return True
    elif check_up_right_diagonal_win(board, row, col, limit, player, rows_count, cols_count):
        return True


def check_horizontal_win(board, limit, player):
    for row in range(len(board) -1, -1, -1):
        count = 0
        for col in range(len(board[row])):
            if board[row][col] == player:
                count += 1
                if count == limit:
                    return True
            else:
                count = 0
    return False


def check_vertical_win(board, limit, player):
    for col in range(len(board[0])):
        count = 0
        for row in range(len(board) -1, -1, -1):
            if board[row][col] == player:
                count += 1
                if count == limit:
                    return True
            else:
                count = 0
    return False


def check_down_left_diagonal_win(board, row_index, col_index, limit, player, rows_count, cols_count):
    counter = 0
    while rows_and_cols_in_range(row_index, col_index, rows_count, cols_count) and counter < limit:
        counter += 1
        if board[row_index][col_index] == player and counter == limit:
            return True

        row_index += 1
        col_index -= 1

    return False


def check_down_right_diagonal_win(board, row_index, col_index, limit, player, rows_count, cols_count):
    counter = 0
    while rows_and_cols_in_range(row_index, col_index, rows_count, cols_count) and counter < limit:
        counter += 1
        if board[row_index][col_index] == player and counter == limit:
            return True

        row_index += 1
        col_index += 1

    return False


def check_up_left_diagonal_win(board, row_index, col_index, limit, player, rows_count, cols_count):
    counter = 0
    while rows_and_cols_in_range(row_index, col_index, rows_count, cols_count) and counter < limit:
        counter += 1
        if board[row_index][col_index] == player and counter == limit:
            return True

        row_index -= 1
        col_index -= 1

    return False


def check_up_right_diagonal_win(board, row_index, col_index, limit, player, rows_count, cols_count):
    counter = 0
    while rows_and_cols_in_range(row_index, col_index, rows_count, cols_count) and counter < limit:
        counter += 1
        if board[row_index][col_index] == player and counter == limit:
            return True

        row_index -= 1
        col_index += 1

    return False


def rows_and_cols_in_range(rows, cols, rows_count, cols_count):
    if 0 <= rows < rows_count and 0 <= cols < cols_count:
        return True
    return False


def is_choice_in_range(player_choice, board):
    if 0 <= player_choice < len(board[0]):
        return True
    return False


def switch_players(player):
    if player == 1:
        return 2
    return 1


def free_cells(*args):
    board, choice = args
    for row in range(len(board)-1, -1, -1):
        for col in range(len(board[row])):
            if col == choice and board[row][col] == 0:
                board[row][col] = player
                return True
            continue
    return False


def get_row_and_col(*args):
    board, choice = args
    for row in range(len(board) - 1, -1, -1):
        for col in range(len(board[row])):
            if col == choice and board[row][col] == 0:
                return row, col
            continue
    return False


def enter_player_choice(player):
    print(f'Player {player} please choose a column')
    return int(input()) - 1


def invalid_range_choice(col_choice, board):
    print('Invalid range')
    print(f'Please choose another column between 0 and {len(play_board)}', end='\n')


def no_free_cells_col(col_choice):
    print(f'No free cells in column {player_choice_col + 1}')
    print(f'Please choose another column', end='\n')


def print_player_board(board):
    for row in range(len(board)):
        print(f"{' '.join(map(str, board[row]))}")


player = 1
play_board = create_play_board()


while True:
    player_choice_col = enter_player_choice(player)
    if is_choice_in_range(player_choice_col, play_board):
        if get_row_and_col(play_board, player_choice_col):
            free_row, free_col = get_row_and_col(play_board, player_choice_col)
            if free_cells(play_board, player_choice_col):
                if winning_condition(play_board, free_row, free_col, WIN_LIMIT_CONDITION, player, DEFAULT_ROWS_COUNT, DEFAULT_COLUMNS_COUNT):
                    print_player_board(play_board)
                    print(f"The Winner is player {player}", end='\n')
                    print(f"Do yuo want another game? Y/N")
                    player_choice = input()
                    if player_choice == 'Y':
                        play_board = create_play_board()
                        player = 1
                        continue
                    else:
                        print(f"The Winner is player {player}", end='\n')
                        print_player_board(play_board)
                        break
                else:
                    player = switch_players(player)
                    print_player_board(play_board)
                    continue
            else:
                # every time the player don't choose correct column or the column is full, the player will be changed
                no_free_cells_col(player_choice_col)
                player = switch_players(player)
                print_player_board(play_board)
        else:
            # every time the player don't choose correct column or the column is full, the player will be changed
            no_free_cells_col(player_choice_col)
            player = switch_players(player)
            print_player_board(play_board)
    else:
        invalid_range_choice(player_choice_col, play_board)
        player = switch_players(player)
        print_player_board(play_board)
        continue

print('Good Bye!')

