budget = float(input())
nights = int(input())
price_per_nights = float(input())
percent_additional_expenses = int(input())

if nights > 7:
    price_per_nights = price_per_nights * 0.95

total_expenses = (nights * price_per_nights)
additional_expenses = (budget * percent_additional_expenses) / 100
total_expenses = total_expenses + additional_expenses


if budget >= total_expenses:
    diff = budget - total_expenses
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    diff = total_expenses - budget
    print(f'{diff:.2f} leva needed.')