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


def winning_condition(board, limit, player):
    if check_horizontal_win(board, limit, player):
        return True
    elif check_vertical_win(board, limit, player):
        return True
    elif check_left_to_right_diagonal_win(board, player):
        return True
    elif check_right_to_left_diagonal_win(board, player):
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


def check_left_to_right_diagonal_win(board, player):
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player and board[3][3] == player) or \
            (board[1][1] == player and board[2][2] == player and board[3][3] == player and board[4][4] == player) or \
            (board[2][2] == player and board[3][3] == player and board[4][4] == player and board[5][5] == player):
        return True

    elif (board[1][0] == player and board[2][1] == player and board[3][2] == player and board[4][3] == player) or \
            (board[2][1] == player and board[3][2] == player and board[4][3] == player and board[5][4] == player):
        return True

    elif board[2][0] == player and board[3][1] == player and board[4][2] == player and board[5][3] == player:
        return True

    elif (board[0][1] == player and board[1][2] == player and board[2][3] == player and board[3][4] == player) or \
            (board[1][2] == player and board[2][3] == player and board[3][4] == player and board[4][5] == player) or \
            (board[2][3] == player and board[3][4] == player and board[4][5] == player and board[5][6] == player):
        return True

    elif (board[0][2] == player and board[1][3] == player and board[2][4] == player and board[3][5] == player) or \
            (board[1][3] == player and board[2][4] == player and board[3][5] == player and board[4][6] == player) or \
            (board[0][3] == player and board[1][4] == player and board[2][5] == player and board[3][6] == player):
        return True


def check_right_to_left_diagonal_win(board, player):
    if (board[0][3] == player and board[1][2] == player and board[2][1] == player and board[3][0] == player) or \
            (board[0][4] == player and board[1][3] == player and board[2][2] == player and board[3][1] == player) or \
            (board[1][3] == player and board[2][2] == player and board[3][1] == player and board[4][0] == player):
        return True

    elif (board[0][5] == player and board[1][4] == player and board[2][3] == player and board[3][2] == player) or \
            (board[1][4] == player and board[2][3] == player and board[3][2] == player and board[4][1] == player) or \
            (board[2][3] == player and board[3][2] == player and board[4][1] == player and board[5][0] == player):
        return True

    elif (board[0][6] == player and board[1][5] == player and board[2][4] == player and board[3][3] == player) or \
            (board[1][5] == player and board[2][4] == player and board[3][3] == player and board[4][2] == player) or \
            (board[2][4] == player and board[3][3] == player and board[4][2] == player and board[5][1] == player):
        return True

    elif (board[1][6] == player and board[2][5] == player and board[3][4] == player and board[4][3] == player) or \
            (board[2][5] == player and board[3][4] == player and board[4][3] == player and board[5][2] == player):
        return True

    elif board[2][6] == player and board[3][5] == player and board[4][4] == player and board[5][3] == player:
        return True


def is_choice_in_range(player_choice, board):
    if 0 <= player_choice < len(board[0]):
        return True
    return False


def switch_players(player):
    if player == 1:
        return 2
    return 1


def free_cells(board, choice):
    row = 0
    for row in range(len(board)-1, -1, -1):
        for col in range(len(board[row])):
            if col == choice and board[row][col] == 0:
                board[row][col] = player
                return True
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


win_limit = 4
player = 1
play_board = create_play_board()

while True:
    player_choice_col = enter_player_choice(player)

    if is_choice_in_range(player_choice_col, play_board):
        if free_cells(play_board, player_choice_col):
            if winning_condition(play_board, win_limit, player):
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

            player = switch_players(player)
            print_player_board(play_board)
            continue
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

