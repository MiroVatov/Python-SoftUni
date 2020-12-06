current_points = 301
player_name = input()
command = input()
sucesfull_shots = 0
unsucesfull_shots = 0

while command != 'Retire':
    points = int(input())

    if command == 'Single':
        points = points
    elif command == 'Double':
        points *= 2
    elif command == 'Triple':
        points *= 3

    if points > current_points:
       unsucesfull_shots += 1

    elif points <= current_points:
        sucesfull_shots += 1
        current_points -= points
    if current_points == 0:
        break
    command = input()

if command == 'Retire':
    print(f'{player_name} retired after {unsucesfull_shots} unsuccessful shots.')
else:
    print(f'{player_name} won the leg with {sucesfull_shots} shots.')


