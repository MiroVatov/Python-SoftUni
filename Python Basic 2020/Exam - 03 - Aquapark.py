month = input()
hours = int(input())
people = int(input())
time = input()

price = 0

if time == 'day':
    if month == 'march' or month == 'april' or month == 'may':
        price = 10.50
        if people >= 4:
            price = price * 0.90
        if hours >= 5:
            price = price * 0.50
    elif month == 'june' or month == 'july' or month == 'august':
        price = 12.60
        if people >= 4:
            price = price * 0.90
        if hours >= 5:
            price = price * 0.50
elif time == 'night':
    if month == 'march' or month == 'april' or month == 'may':
        price = 8.40
        if people >= 4:
            price = price * 0.90
        if hours >= 5:
            price = price * 0.50
    elif month == 'june' or month == 'july' or month == 'august':
        price = 10.20
        if people >= 4:
            price = price * 0.90
        if hours >= 5:
            price = price * 0.50
total_cost = (people * price) * hours

print(f'Price per person for one hour: {price:.2f}')
print(f'Total cost of the visit: {total_cost:.2f}')