base_camp = 5364
target_amount = 8848

day = 1
command = input()

while command != 'END':
    if command == 'Yes':
        day += 1
    elif command == 'No':
        day = day
    meters = int(input())
    base_camp += meters
    if base_camp >= target_amount or day >= 5:
        break

    command = input()

if base_camp >= target_amount:
    print(f'Goal reached for {day} days!')
else:
    print(f'Failed!')
    print(f'{base_camp}')