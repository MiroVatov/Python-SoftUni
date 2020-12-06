
first_player = False
second_player = False

first_player_count = 0
second_player_count = 0

total_squares = 0

while total_squares < 9:
    move = input().split(" ")

    for a in move:
        if int(a) == 1:
            first_player_count += 1
            second_player_count = 0
            if first_player_count == 3:
                first_player = True
                print(f"First player won")
                break

        elif int(a) == 2:
            second_player_count += 1
            first_player_count = 0
            if second_player_count == 3:
                second_player = True
                print(f"Second player won")
                break
        else:
            pass
        total_squares += 1
    if first_player:
        break
    elif second_player:
        break

if not first_player and not second_player and total_squares == 9:
    print(f"Draw!")