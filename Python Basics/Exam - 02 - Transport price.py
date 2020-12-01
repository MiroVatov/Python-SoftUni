
kilometers = int(input())
day_or_night = input()
minimum_price = 0
vehicle_price = 0
distance_price = 0

if kilometers >= 100:
    vehicle_price = 0.06
    distance_price = vehicle_price * kilometers
elif kilometers >= 20:
    vehicle_price = 0.09
    distance_price = vehicle_price * kilometers
else:
    if day_or_night == 'day':
        vehicle_price = 0.79
    elif day_or_night == 'night':
        vehicle_price = 0.90
    distance_price = 0.70 + (vehicle_price * kilometers)

print(f'{distance_price:.2f}')