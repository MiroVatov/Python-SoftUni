type_of_fuel = input()
fuel_quantity = float(input())
club_card = input()

gasoline_price =  2.22
dielsel_price = 2.33
gas_price = 0.93

fuel_price = 0

if type_of_fuel == 'Gasoline':
    if club_card == 'Yes':
        fuel_price = gasoline_price - 0.18
    elif club_card == 'No':
        fuel_price = gasoline_price
elif type_of_fuel == 'Diesel':
    if club_card == 'Yes':
        fuel_price = dielsel_price - 0.12
    elif club_card == 'No':
        fuel_price = dielsel_price
elif type_of_fuel == 'Gas':
    if club_card == 'Yes':
        fuel_price = gas_price - 0.08
    elif club_card == 'No':
        fuel_price = gas_price

if 20 <= fuel_quantity <= 25:
    fuel_price = fuel_price * 0.92
elif fuel_quantity > 25:
    fuel_price = fuel_price * 0.90

print(f'{fuel_price * fuel_quantity:.2f} lv.')