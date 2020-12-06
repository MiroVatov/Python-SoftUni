type_of_fuel = input()
fuel_liters = int(input())

if type_of_fuel != 'Gas' and type_of_fuel != 'Gasoline' and type_of_fuel != 'Diesel':
    print(f'Invalid fuel!')
elif fuel_liters >= 25:
    print(f'You have enough {type_of_fuel.lower()}.')
elif fuel_liters < 25:
    print(f'Fill your tank with {type_of_fuel.lower()}!')
