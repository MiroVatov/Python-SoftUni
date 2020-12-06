trunk_capacity = float(input())
command = input()
suitcase_count = 0
while command != 'End':
    suitcase = float(command)

    if suitcase > trunk_capacity:
        print('No more space!')
        break
    suitcase_count += 1
    if suitcase_count % 3 == 0:
        suitcase = suitcase * 1.10
    trunk_capacity -= suitcase
    if trunk_capacity <= 0:
        suitcase_count -= 1
        print('No more space!')
        break
    command = input()
if command == 'End':
    print('Congratulations! All suitcases are loaded!')

print(f'Statistic: {suitcase_count} suitcases loaded.')