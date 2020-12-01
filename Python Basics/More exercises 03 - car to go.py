budget = float(input())
season = input()

class_type = ''
car_type = ''
price = 0
car_price = 0

if budget <= 100:
    class_type = 'Economy class'
    if season == 'Summer':
        car_type = 'Cabrio'
        car_price = budget * 0.35

    elif season == 'Winter':
        car_price = budget * 0.65
        car_type = 'Jeep'
elif 100 < budget <= 500:
    class_type = 'Compact class'
    if season == 'Summer':
        car_price = budget * 0.45
        car_type = 'Cabrio'

    elif season == 'Winter':
        car_price = budget * 0.80
        car_type = 'Jeep'

elif budget > 500:
    class_type = 'Luxury class'
    car_price = budget * 0.90
    car_type = 'Jeep'

print(f'{class_type}')
print(f'{car_type} - {car_price:.2f}')