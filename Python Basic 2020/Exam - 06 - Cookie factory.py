badges_for_day = int(input())
batch_number = 0

while batch_number <= badges_for_day:
    command = input()
    flour_count = 0
    sugar_count = 0
    eggs_count = 0
    while command != 'Bake!':

        if command == 'flour':
            flour_count += 1
        elif command == 'sugar':
            sugar_count += 1
        elif command == 'eggs':
            eggs_count += 1
        command = input()

    if command == 'Bake!' and sugar_count >= 1 and eggs_count >= 1 and flour_count >= 1:
        batch_number += 1
        print(f'Baking batch number {batch_number}...')
    else:
        print(f'The batter should contain flour, eggs and sugar!')
