DART_LIMIT = 7

first_player_name, second_player_name = input().split(', ')

first_player_data = {"name": first_player_name, "initial_score": 501, "throws": 0}
second_player_data = {"name": second_player_name, "initial_score": 501, "throws": 0}

dart_board = list(input().split() for _ in range(7))

winner = ''
turn = 0


def check_if_shot_is_in_dartboard(row, col):
    if (row < 0 or col < 0) or (row >= DART_LIMIT or col >= DART_LIMIT):
        return False
    return True


def check_sum_of_four(row, col):
    sum_of_four = int(int(dart_board[row][0]) + int(dart_board[row][-1]) + int(dart_board[0][col]) + int(
        dart_board[-1][col]))
    return sum_of_four


while True:
    player = ''

    if turn % 2 == 0:
        player = first_player_data
    else:
        player = second_player_data

    turn += 1

    throw_row, throw_col = input().split(', ')
    player_shot_row = int(throw_row.replace('(', ''))
    player_shot_col = int(throw_col.replace(')', ''))

    if not check_if_shot_is_in_dartboard(player_shot_row, player_shot_col):
        player["throws"] += 1
        continue

    sum_of_four_corresponding_numbers = check_sum_of_four(player_shot_row, player_shot_col)

    if dart_board[player_shot_row][player_shot_col].isdigit():
        player["initial_score"] -= int(dart_board[player_shot_row][player_shot_col])
        player["throws"] += 1

    elif dart_board[player_shot_row][player_shot_col] == "D":
        player["initial_score"] -= sum_of_four_corresponding_numbers * 2
        player["throws"] += 1

    elif dart_board[player_shot_row][player_shot_col] == "T":
        player["initial_score"] -= sum_of_four_corresponding_numbers * 3
        player["throws"] += 1

    if player["initial_score"] <= 0:
        winner = player
        break

    elif dart_board[player_shot_row][player_shot_col] == "B":
        player["throws"] += 1
        winner = player
        break


print(f"{winner['name']} won the game with {winner['throws']} throws!")
