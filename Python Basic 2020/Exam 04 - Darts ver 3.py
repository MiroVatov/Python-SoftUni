player_name = input()

strating_points = 301
total_points = 0
successfull_shots = 0
unsucesssfull_shots = 0
command = input()
won = False
while command != 'Retire':

    points = 0

    points = int(input())
    if command == 'Single':
        points = points

    elif command == 'Double':
        points = points * 2

    elif command == 'Triple':
        points = points * 3

    if points > strating_points:
        unsucesssfull_shots += 1
        command = input()
        continue
    elif points <= strating_points:
        successfull_shots += 1
    if points == strating_points:
        won = True
        break
    strating_points -= points
    command = input()
if command == 'Retire':
    print(f'{player_name} retired after {unsucesssfull_shots} unsuccessful shots.')
elif won == True:
    print(f'{player_name} won the leg with {successfull_shots} shots.')

