tank_capacity = 255
n = int(input())
tank = 0

for i in range(1, n + 1):
    liters = int(input())

    if liters > tank_capacity:
        print('Insufficient capacity!')
    else:
        tank += liters
        tank_capacity -= liters

print(f'{tank}')