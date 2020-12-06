pirateship_status = input().split('>')
warship_status = input().split('>')
maximum_health = int(input())
pirateship_status = [int(n) for n in pirateship_status]
warship_status = [int(i) for i in warship_status]
command = input().split()
pirateship_good = True
warship_good = True

while command[0] != 'Retire':
    if command[0] == 'Fire':
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(warship_status):
            warship_status[index] -= damage
            if int(warship_status[index]) <= 0:
                print(f'You won! The enemy ship has sunken.')
                warship_good = False
                break

    elif command[0] == 'Defend':
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])

        if 0 <= start_index < len(pirateship_status) and 0 <= end_index < len(pirateship_status):
            for i in range(start_index, end_index + 1):
                pirateship_status[i] -= damage
                if pirateship_status[i] <= 0:
                    print(f'You lost! The pirate ship has sunken.')
                    pirateship_good = False
                    break

    elif command[0] == 'Repair':
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(pirateship_status):
            if (pirateship_status[index] + health) < maximum_health:
                pirateship_status[index] += health
            else:
                pirateship_status[index] = maximum_health

    elif command[0] == 'Status':
        repair_limit = int(0.20 * maximum_health)
        sections_for_repair = 0
        for s in pirateship_status:
            if int(s) < repair_limit:
                sections_for_repair += 1

        print(f'{sections_for_repair} sections need repair.')

    command = input().split()


if pirateship_good and warship_good:
    print(f'Pirate ship status: {sum(pirateship_status)}')
    print(f'Warship status: {sum(warship_status)}')

