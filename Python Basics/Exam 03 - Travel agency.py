destination_name = input()
package_type = input()
vip_discount = input()
days = int(input())
negative_days = False
invalid_destination = False
price_per_day = 0

if destination_name == 'Bansko' or destination_name == 'Borovets':
    if package_type == 'withEquipment':
        price_per_day = 100
        if vip_discount == 'yes':
            price_per_day = price_per_day * 0.90
        elif vip_discount == 'no':
            price_per_day = price_per_day
    elif package_type == 'noEquipment':
        price_per_day = 80
        if vip_discount == 'yes':
            price_per_day = price_per_day * 0.95
        elif vip_discount == 'no':
            price_per_day = price_per_day


elif destination_name == 'Varna' or destination_name == 'Burgas':
    if package_type == 'withBreakfast':
        price_per_day = 130
        if vip_discount == 'yes':
            price_per_day = price_per_day * 0.88
        elif vip_discount == 'no':
            price_per_day = price_per_day
    elif package_type == 'noBreakfast':
        price_per_day = 100
        if vip_discount == 'yes':
            price_per_day = price_per_day * 0.97
        elif vip_discount == 'no':
            price_per_day = price_per_day

total_price = price_per_day * days

if days < 1:
    negative_days = True
if destination_name != 'Bansko' and destination_name != 'Borovets' and destination_name != 'Varna' and destination_name != 'Burgas'\
    or package_type != 'noEquipment' and package_type != 'withEquipment' and package_type != 'noBreakfast' and package_type != 'withBreakfast':
    invalid_destination = True


if days > 7 and not negative_days and not invalid_destination:
    total_price = price_per_day * (days - 1)
    print(f'The price is {total_price:.2f}lv! Have a nice time!')
elif 1 <= days <= 7 and not negative_days and not invalid_destination:
    print(f'The price is {total_price:.2f}lv! Have a nice time!')

if negative_days == True:
    print(f'Days must be positive number!')
if invalid_destination == True:
    print(f'Invalid input!')
