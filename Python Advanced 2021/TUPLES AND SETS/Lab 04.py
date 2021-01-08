n_cars = int(input())

cars_lst = []

for _ in range(n_cars):
    direction, reg_num = input().split(', ')
    if direction == 'IN':
        cars_lst.append(reg_num)
    elif direction == 'OUT':
        cars_lst.remove(reg_num)


if cars_lst:
    cars_lst = set(cars_lst)
    for c in cars_lst:
        print(c)
else:
    print("Parking Lot is Empty")