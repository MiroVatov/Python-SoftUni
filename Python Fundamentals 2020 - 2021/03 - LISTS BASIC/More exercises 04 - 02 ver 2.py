first_win = False
second_win = False
actions = []

for r in range(3):

    actions.append([int(row) for row in input().split()])

if actions[0][0] == 1 and actions[1][0] == 1 and actions[2][0] == 1:
    first_win = True
elif actions[0][2] == 1 and actions[1][2] == 1 and actions[2][2] == 1:
    first_win = True
elif actions[0][1] == 1 and actions[1][1] == 1 and actions[2][1] == 1:
    first_win = True
elif actions[0][0] == 1 and actions[0][1] == 1 and actions[0][2] == 1:
    first_win = True
elif actions[1][0] == 1 and actions[1][1] == 1 and actions[1][2] == 1:
    first_win = True
elif actions[2][0] == 1 and actions[2][1] == 1 and actions[2][2] == 1:
    first_win = True
elif actions[0][0] == 1 and actions[1][1] == 1 and actions[2][2] == 1:
    first_win = True
elif actions[0][2] == 1 and actions[1][1] == 1 and actions[2][0] == 1:
    first_win = True

if actions[0][0] == 2 and actions[1][0] == 2 and actions[2][0] == 2:
    second_win = True
elif actions[0][2] == 2 and actions[1][2] == 2 and actions[2][2] == 2:
    second_win = True
elif actions[0][1] == 2 and actions[1][1] == 2 and actions[2][1] == 2:
    second_win = True
elif actions[0][0] == 2 and actions[0][1] == 2 and actions[0][2] == 2:
    second_win = True
elif actions[1][0] == 2 and actions[1][1] == 2 and actions[1][2] == 2:
    second_win = True
elif actions[2][0] == 2 and actions[2][1] == 2 and actions[2][2] == 2:
    second_win = True
elif actions[0][0] == 2 and actions[1][1] == 2 and actions[2][2] == 2:
    second_win = True
elif actions[0][2] == 2 and actions[1][1] == 2 and actions[2][0] == 2:
    second_win = True


if first_win:
    print(f"First player won")
elif second_win:
    print(f"Second player won")
else:
    print(f"Draw!")