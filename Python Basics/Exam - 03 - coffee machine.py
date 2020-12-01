type_drink = input()
sugar_level = input()
drinks_qty = int(input())

drink_price = 0
total_drinks_price = 0

if type_drink == 'Espresso':
    if sugar_level == 'Without':
        drink_price = 0.90
    elif sugar_level == 'Normal':
        drink_price = 1
    elif sugar_level == 'Extra':
        drink_price = 1.2

elif type_drink == 'Cappuccino':
    if sugar_level == 'Without':
        drink_price = 1
    elif sugar_level == 'Normal':
        drink_price = 1.2
    elif sugar_level == 'Extra':
        drink_price = 1.6

elif type_drink == 'Tea':
    if sugar_level == 'Without':
        drink_price = 0.5
    elif sugar_level == 'Normal':
        drink_price = 0.6
    elif sugar_level == 'Extra':
        drink_price = 0.7

if sugar_level == 'Without':
    drink_price = drink_price * 0.65
if type_drink == 'Espresso' and drinks_qty >= 5:
    drink_price = drink_price * 0.75

total_drinks_price = drink_price * drinks_qty

if total_drinks_price > 15:
    total_drinks_price = total_drinks_price * 0.80

print(f'You bought {drinks_qty} cups of {type_drink} for {total_drinks_price:.2f} lv.')