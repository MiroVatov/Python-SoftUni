#VIP_ticket = 499.99
#Normal_ticket = 249.99
budget = float(input())
category_ticket = input()
number_of_people = int(input())
transport_money = 0
budget_left = 0
ticket_price = 0
if 1 <= number_of_people <= 4:
    transport_money = budget * 0.75
elif 5 <= number_of_people <= 9:
    transport_money = budget * 0.60
elif 10 <= number_of_people <= 24:
    transport_money = budget * 0.50
elif 25 <= number_of_people <= 49:
    transport_money = budget * 0.40
elif number_of_people >= 50:
    transport_money = budget * 0.25

budget_left = budget - transport_money


if category_ticket == 'VIP':
    ticket_price = 499.99
if category_ticket == 'Normal':
    ticket_price = 249.99

total_ticket_price = ticket_price * number_of_people

if budget_left >= total_ticket_price:
    diff = budget_left - total_ticket_price
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    diff = total_ticket_price - budget_left
    print(f'Not enough money! You need {diff:.2f} leva.')