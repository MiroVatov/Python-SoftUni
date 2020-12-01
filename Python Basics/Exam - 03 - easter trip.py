destination = input()
dates_between = input()
nights = int(input())

price_per_night = 0

if destination == 'France':
    if dates_between == '21-23':
        price_per_night = 30
    elif dates_between == '24-27':
        price_per_night = 35
    elif dates_between == '28-31':
        price_per_night = 40
elif destination == 'Italy':
    if dates_between == '21-23':
        price_per_night = 28
    elif dates_between == '24-27':
        price_per_night = 32
    elif dates_between == '28-31':
        price_per_night = 39

elif destination == 'Germany':
    if dates_between == '21-23':
        price_per_night = 32
    elif dates_between == '24-27':
        price_per_night = 37
    elif dates_between == '28-31':
        price_per_night = 43

total_expenses = price_per_night * nights

print(f'Easter trip to {destination} : {total_expenses:.2f} leva.')