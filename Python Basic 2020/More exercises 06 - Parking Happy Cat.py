number_of_days = int(input())
number_of_hours = int(input())
parking_price = 0
total_sum = 0

for days in range(1, number_of_days + 1):
    total_per_day = 0
    for hours in range(1, number_of_hours + 1):
        if days % 2 == 0 and hours % 2 != 0:
            parking_price = 2.50
        elif days % 2 != 0 and hours % 2 == 0:
            parking_price = 1.25
        else:
            parking_price = 1
        total_per_day += parking_price
    print(f'Day: {days} - {total_per_day:.2f} leva')
    total_sum += total_per_day

print(f'Total: {total_sum:.2f} leva')