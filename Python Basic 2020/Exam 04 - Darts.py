player_name = input()

strating_points = 301
total_points = 0
successfull_shots = 0
unsucesssfull_shots = 0

while strating_points > 0:
    command = input()
    points = 0
    if command == 'Retire':
        break
    points = int(input())
    if command == 'Single':
        points = points

    elif command == 'Double':
        points = points * 2

    elif command == 'Triple':
        points = points * 3

    if points > strating_points:
        unsucesssfull_shots += 1
        continue
    elif points <= strating_points:
        successfull_shots += 1
    if points == strating_points:
        break
    strating_points -= points
if command == 'Retire':
    print(f'{player_name} retired after {unsucesssfull_shots} unsuccessful shots.')
else:
    print(f'{player_name} won the leg with {successfull_shots} shots.')

