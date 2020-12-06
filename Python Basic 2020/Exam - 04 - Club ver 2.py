income_needed = float(input())

total_income = 0

while total_income < income_needed:
    cocktail_name = input()
    if cocktail_name == 'Party!':
        diff = income_needed - total_income
        print(f'We need {diff:.2f} leva more.')
        break

    number_of_cocktails = int(input())
    cocktail_price = len(cocktail_name)
    current_income = cocktail_price * number_of_cocktails

    if current_income % 2 != 0:
        current_income = current_income * 0.75
    total_income += current_income

if total_income >= income_needed:
    print(f'Target acquired.')

print(f'Club income - {total_income:.2f} leva.')