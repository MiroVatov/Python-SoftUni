budget = float(input())
season = input()

destination = ''
type_of_vacation = ''
vacation_money = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        vacation_money = budget * 0.30
        type_of_vacation = 'Camp'
    elif season == 'winter':
        vacation_money = budget * 0.70
        type_of_vacation = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        vacation_money = budget * 0.40
        type_of_vacation = 'Camp'
    elif season == 'winter':
        vacation_money = budget * 0.80
        type_of_vacation = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    vacation_money = budget * 0.90
    type_of_vacation = 'Hotel'
print(f'Somewhere in {destination}')
print(f'{type_of_vacation} - {vacation_money:.2f}')