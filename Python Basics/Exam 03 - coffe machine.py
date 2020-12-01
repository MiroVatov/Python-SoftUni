drink = input()
sugar_level = input()
drinks_number = int(input())

drink_price = 0

if drink == 'Espresso':
    if sugar_level == 'Without':
        drink_price = 0.90
    elif sugar_level == 'Normal':
        drink_price = 1
    elif sugar_level == 'Extra':
        drink_price = 1.20
elif drink == 'Cappuccino':
    if sugar_level == 'Without':
        drink_price = 1
    elif sugar_level == 'Normal':
        drink_price = 1.20
    elif sugar_level == 'Extra':
        drink_price = 1.60
elif drink == 'Tea':
    if sugar_level == 'Without':
        drink_price = 0.50
    elif sugar_level == 'Normal':
        drink_price = 0.60
    elif sugar_level == 'Extra':
        drink_price = 0.70

total_bill = drink_price * drinks_number

if sugar_level == 'Without':
    total_bill = total_bill * 0.65
if drink == 'Espresso' and drinks_number >= 5:
    total_bill = total_bill * 0.75
if total_bill > 15:
    total_bill = total_bill * 0.80

print(f'You bought {drinks_number} cups of {drink} for {total_bill:.2f} lv.')
