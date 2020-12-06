eggs_available = int(input())

command = input()
total_eggs_sold = 0
while command != 'Close':
    eggs_num = int(input())
    if command == 'Buy':
        if eggs_available < eggs_num:
            break
        total_eggs_sold += eggs_num
        eggs_available -= eggs_num
    elif command == 'Fill':
        eggs_available += eggs_num

    command = input()
if command == 'Close':
    print('Store is closed!')
    print(f'{total_eggs_sold} eggs sold.')
else:
    print('Not enough eggs in store!')
    print(f'You can buy only {eggs_available}.')