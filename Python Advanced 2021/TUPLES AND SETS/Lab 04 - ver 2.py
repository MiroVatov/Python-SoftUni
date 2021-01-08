n = int(input())

parking = set()
for _ in range(n):
    direction, reg_num = input().split(', ')
    if direction == 'IN':
        parking.add(reg_num)
    elif direction == 'OUT':
        parking.remove(reg_num)
if parking:
    print('\n'.join(parking))
else:
    print('Parking Lot is Empty')