contract_lenght = input()
contract_type = input()
mobile_internet = input()
months = int(input())
month_price = 0
total_bill = 0

if contract_type == 'Small':
    if contract_lenght == 'one':
        month_price = 9.98
    elif contract_lenght == 'two':
        month_price = 8.58
elif contract_type == 'Middle':
    if contract_lenght == 'one':
        month_price = 18.99
    elif contract_lenght == 'two':
        month_price = 17.09
elif contract_type == 'Large':
    if contract_lenght == 'one':
        month_price = 25.98
    elif contract_lenght == 'two':
        month_price = 23.59
elif contract_type == 'ExtraLarge':
    if contract_lenght == 'one':
        month_price = 35.99
    elif contract_lenght == 'two':
        month_price = 31.79

if mobile_internet == 'yes':
    if month_price <= 10:
        month_price += 5.50
    elif month_price <= 30:
        month_price += 4.35
    elif month_price > 30:
        month_price += 3.85
total_bill = months * month_price
if contract_lenght == 'two':
    total_bill = (total_bill * 96.25) / 100
print(f'{total_bill:.2f} lv.')