budget = int(input())
season = input()
fisherman_qty = int(input())
boat_price = 0

if season == 'Spring':
    boat_price = 3000
    if fisherman_qty <= 6:
        boat_price = boat_price * 0.9
    elif 7 < fisherman_qty <= 11:
        boat_price = boat_price * 0.85
    elif fisherman_qty > 12:
        boat_price = boat_price * 0.75

elif season == 'Summer' or season == 'Autumn':
    boat_price = 4200
    if fisherman_qty <= 6:
        boat_price = boat_price * 0.9
    elif 7 < fisherman_qty <= 11:
        boat_price = boat_price * 0.85
    elif fisherman_qty > 12:
        boat_price = boat_price * 0.75

elif season == 'Winter':
    boat_price = 2600
    if fisherman_qty <= 6:
        boat_price = boat_price * 0.9
    elif 7 < fisherman_qty <= 11:
        boat_price = boat_price * 0.85
    elif fisherman_qty > 12:
        boat_price = boat_price * 0.75

if fisherman_qty % 2 == 0 and season != 'Autumn':
    boat_price = boat_price * 0.95

money_left = abs(budget - boat_price)

if budget >= boat_price:
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    print(f'Not enough money! You need {money_left:.2f} leva.')