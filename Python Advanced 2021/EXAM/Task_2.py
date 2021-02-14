# P -> player
# numbers -> coins
# Wall -> X

import math


def valid_index(size, row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


valid_commands = ['up', 'down', 'left', 'right']

PLAYER = 'P'
WALL = 'X'

size = int(input())

play_field = [[] * size for _ in range(size)]

player_current_row = 0
player_current_col = 0

for ind in range(len(play_field)):
    play_field[ind] = input().split()
    if PLAYER in play_field[ind]:
        player_current_row, player_current_col = ind, play_field[ind].index(PLAYER)

successful_moves = []

coins_collected = 0

success = False

fail = False

while True:

    if coins_collected >= 100:
        success = True
        break
        # TODO check if has to break here or leave
    command = input()

    if command not in valid_commands:
        continue

    if command == 'up':
        player_current_row -= 1

    elif command == 'down':
        player_current_row += 1

    elif command == 'left':
        player_current_col -= 1

    elif command == 'right':
        player_current_col += 1

    if not valid_index(size, player_current_row, player_current_col):
        fail = True
        break

    if play_field[player_current_row][player_current_col] == WALL:
        fail = True
        break

    coins_collected += int(play_field[player_current_row][player_current_col])
    successful_moves.append([player_current_row, player_current_col])


if success:
    print(f"You won! You've collected {math.floor(coins_collected)} coins.")
    print(f"Your path: ")
    for line in successful_moves:
        print(f"{line}")

else:
    coins_collected *= 0.50
    print(f"Game over! You've collected {math.floor(coins_collected)} coins.")
    print(f"Your path: ")
    for line in successful_moves:
        print(f"{line}")
