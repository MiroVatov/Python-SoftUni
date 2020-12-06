inherited_money = float(input())
year_to_live = int(input())
#expense_per_year = 0
total_expenses = 0
age = 18
left_money = 0

for i in range(1800, year_to_live + 1):
    if i % 2 == 0:
        expense_per_year = 12000

    else:
        expense_per_year = 12000 + (age * 50)
    age += 1
    total_expenses += expense_per_year
    left_money = abs(inherited_money - total_expenses)

if inherited_money >= total_expenses:
    print(f'Yes! He will live a carefree life and will have {left_money:.2f} dollars left.' )
else:
    print(f'He will need {left_money:.2f} dollars to survive.')