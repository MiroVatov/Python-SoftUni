trunk_capacity = float(input())
suitcases_qty = 0
suitcase = input()
space = True
while suitcase != 'End':
    suitcase = float(suitcase)
    if trunk_capacity <= suitcase:
        space = False
        break
    suitcases_qty += 1
    trunk_capacity -= suitcase
    if suitcases_qty % 3 == 0:
        trunk_capacity += suitcase
        suitcase = suitcase + (suitcase * 0.10)
        trunk_capacity -= suitcase

        if trunk_capacity < 0:
            suitcases_qty -= 1
            space = False
            break

    suitcase = input()

if not space:
    print('No more space!')
if space:
    print('Congratulations! All suitcases are loaded!')

print(f'Statistic: {suitcases_qty} suitcases loaded.')