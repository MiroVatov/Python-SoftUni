STARTING_SCORE = 501

player_one, player_two = input().split(', ')

player_one_score = STARTING_SCORE
player_two_score = STARTING_SCORE

play_field = [input().split() for _ in range(7)]

winner = ''

player_turn = 0

players_dict = {player_one: {"score": player_one_score, "turns": 0}, player_two: {"score": player_two_score, "turns": 0}}


def check_if_shot_is_valid(field, player_row, player_col):
    if (player_row < 0 or player_col < 0) or (player_row >= len(field) or player_col >= len(field)):
        return None
    return field[player_row][player_col]


def calculate_score(field, player_row, player_col):
    first_r = int(field[player_row][0])
    last_r = int(field[player_row][-1])
    first_c = int(field[0][player_col])
    last_c = int(field[-1][player_col])
    score = first_r + last_r + first_c + last_c
    return score


while True:
    player_coordinates = input().split(', ')
    (player_shot_row, player_shot_col) = player_coordinates
    player_shot_row = int(player_shot_row.replace('(', ''))
    player_shot_col = int(player_shot_col.replace(')', ''))
    target_hit = check_if_shot_is_valid(play_field, player_shot_row, player_shot_col)

    player_name = ''
    if player_turn % 2 == 0:
        player_name = player_one
    else:
        player_name = player_two

    if target_hit is not None:
        score_to_deduct = 0

        if target_hit.isdigit():
            players_dict[player_name]["score"] -= int(target_hit)

        elif target_hit == "D":
            score_to_deduct = calculate_score(play_field, player_shot_row, player_shot_col)
            players_dict[player_name]["score"] -= (score_to_deduct * 2)

        elif target_hit == "T":
            score_to_deduct = calculate_score(play_field, player_shot_row, player_shot_col)
            players_dict[player_name]["score"] -= (score_to_deduct * 3)

        elif target_hit == "B":
            players_dict[player_name]["score"] = 0

        players_dict[player_name]["turns"] += 1
        player_turn += 1

        if players_dict[player_name]["score"] <= 0:
            winner = player_name
            break
    else:
        players_dict[player_name]["turns"] += 1
        player_turn += 1

print(f"{winner} won the game with {players_dict[winner]['turns']} throws!")


