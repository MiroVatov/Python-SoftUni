film_budget = float(input())
statist_qty = int(input())
statist_clothes = float(input())
discount = 0
decor = 0.10 * film_budget


statist_clothes = statist_qty * statist_clothes

if statist_qty > 150:
    discount = statist_clothes * 0.10
statist_clothes = statist_clothes - discount

total_money = decor + statist_clothes
left_money = abs(film_budget - total_money)

if total_money > film_budget:
    print('Not enough money!')
    print(f'Wingard needs {left_money:.2f} leva more.')
elif total_money <= film_budget:
    print('Action!')
    print(f'Wingard starts filming with {left_money:.2f} leva left.')