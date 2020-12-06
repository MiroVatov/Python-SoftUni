tank_capacity = 255
number_of_flows = int(input())
tank = 0
counter = 0
while counter < number_of_flows:
    liters = int(input())

    if liters > tank_capacity:
        print('Insufficient capacity!')
    else:
        tank += liters
        tank_capacity -= liters
    counter += 1
print(f'{tank}')