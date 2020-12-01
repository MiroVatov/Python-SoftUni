month = input()
hours = int(input())
people_in_group = int(input())
day_or_night = input()
price = 0

if month == 'march' or month == 'april' or month == 'may':
    if day_or_night == 'day':
        price = 10.50
    elif day_or_night == 'night':
        price = 8.4
if month == 'june' or month == 'july' or month == 'august':
    if day_or_night == 'day':
        price = 12.60
    elif day_or_night == 'night':
        price = 10.20
if people_in_group >= 4:
    price = price * 0.90
if hours >= 5:
    price = price * 0.50

total_bill = hours * price * people_in_group

print(f'Price per person for one hour: {price:.2f}')
print(f'Total cost of the visit: {total_bill:.2f}')
