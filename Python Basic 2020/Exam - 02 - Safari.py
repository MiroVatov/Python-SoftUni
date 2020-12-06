budget = float(input())
fuel_needed = float(input())
day_of_week = input()
fuel_price_per_liter = 2.10
gid_price = 100
total_bill = 0

total_bill = (fuel_needed * fuel_price_per_liter) + gid_price

if day_of_week == 'Saturday':
  total_bill = total_bill * 0.90
elif day_of_week == 'Sunday':
    total_bill = total_bill * 0.80
money_left = abs(budget - total_bill)
if budget >= total_bill:
    print(f'Safari time! Money left: {money_left:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {money_left:.2f} lv.')