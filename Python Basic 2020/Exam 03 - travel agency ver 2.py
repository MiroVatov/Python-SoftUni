town = input()
option = input()
vip = input()
days = int(input())

if days > 7:
    days -= 1

if not (town in ("Bansko", "Borovets") and option in ("noEquipment", "withEquipment",)) and not (
        town in ("Varna", "Burgas") and option in ("noBreakfast", "withBreakfast")):
    print(f'Invalid input!')

elif days < 1:
    print(f'Days must be positive number!')

else:
    if town == 'Bansko' or town == 'Borovets':
        if option == 'withEquipment':
            price = 100 * days
            if vip == 'yes':
                price *= 0.9
        elif option == 'noEquipment':
            price = 80 * days
            if vip == 'yes':
                price *= 0.95

    elif town == 'Varna' or town == 'Burgas':
        if option == 'withBreakfast':
            price = 130 * days
            if vip == 'yes':
                price *= 0.88
        elif option == 'noBreakfast':
            price = 100 * days
            if vip == 'yes':
                price *= 0.93

    print(f'The price is {price:.2f}lv! Have a nice time!')