budget = float(input())
laps_num = input()
fan_card = input()
card_type = input()

ticket_price = 0

if card_type == 'Child':
    if laps_num == 'five':
        ticket_price = 7
    elif laps_num == 'ten':
        ticket_price = 11
elif card_type == 'Junior':
    if laps_num == 'five':
        ticket_price = 9
    elif laps_num == 'ten':
        ticket_price = 16
elif card_type == 'Adult':
    if laps_num == 'five':
        ticket_price = 12
    elif laps_num == 'ten':
        ticket_price = 21
elif card_type == 'Profi':
    if laps_num == 'five':
        ticket_price = 18
    elif laps_num == 'ten':
        ticket_price = 32

if fan_card == 'yes':
    ticket_price = ticket_price * 0.80

if budget >= ticket_price:
    diff = budget - ticket_price
    print(f'You bought {card_type} ticket for {laps_num} laps. Your change is {diff:.2f}lv.')
else:
    diff = ticket_price - budget
    print(f'You don\'t have enough money! You need {diff:.2f}lv more.')