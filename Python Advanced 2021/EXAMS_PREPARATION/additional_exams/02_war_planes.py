def move_is_valid(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def print_battle_field(matrix):
    for line in range(len(matrix)):
        print(f"{' '.join(matrix[line])}")


size = int(input())

battle_filed = [[] for _ in range(size)]

EMPTY_FIELD = '.'
TARGET = 't'
PLANE = 'p'

plane_starting_row = 0
plane_starting_col = 0
targets_count = 0
killed_targets = 0
all_targets_killed = False

for row in range(len(battle_filed)):
    battle_filed[row] = list(input().split())
    if PLANE in battle_filed[row]:
        plane_starting_row, plane_starting_col = row, battle_filed[row].index(PLANE)
    if TARGET in battle_filed[row]:
        targets_count += battle_filed[row].count(TARGET)

moves_count = int(input())

plane_current_row, plane_current_col = plane_starting_row, plane_starting_col

for move in range(moves_count):

    command, direction, steps = input().split()

    #  move  -> command
    #  Move the player only if the filed he wants to step on is marked with EMPTY_FIELD
    player_last_row, player_last_col = plane_current_row, plane_current_col

    if command == 'move':
        if direction == 'up':
            plane_current_row -= int(steps)
        elif direction == 'down':
            plane_current_row += int(steps)
        elif direction == 'left':
            plane_current_col -= int(steps)
        elif direction == 'right':
            plane_current_col += int(steps)

        if move_is_valid(plane_current_row, plane_current_col, size) and battle_filed[plane_current_row][plane_current_col] == EMPTY_FIELD:
            battle_filed[player_last_row][player_last_col] = EMPTY_FIELD
            battle_filed[plane_current_row][plane_current_col] = PLANE

        else:
            plane_current_row, plane_current_col = player_last_row, player_last_col

    elif command == 'shoot':
        shoot_row = plane_current_row
        shoot_col = plane_current_col

        if direction == 'up':
            shoot_row -= int(steps)
        elif direction == 'down':
            shoot_row += int(steps)
        elif direction == 'left':
            shoot_col -= int(steps)
        elif direction == 'right':
            shoot_col += int(steps)
        if move_is_valid(shoot_row, shoot_col, size) and battle_filed[shoot_row][shoot_col] != 'x':
            if battle_filed[shoot_row][shoot_col] == TARGET:
                killed_targets += 1
            battle_filed[shoot_row][shoot_col] = 'x'
            if killed_targets == targets_count:
                all_targets_killed = True
                break

if all_targets_killed:
    print(f"Mission accomplished! All {killed_targets} targets destroyed.")
else:
    print(f"Mission failed! {targets_count - killed_targets} targets left.")

print_battle_field(battle_filed)
