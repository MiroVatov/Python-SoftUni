desired_income = float(input())
cocktail_name = input()

number_of_cocktails = 0
total_income = 0
target = False
while cocktail_name != 'Party!':
    cocktail_price = len(cocktail_name)
    number_of_cocktails = int(input())
    current_income = cocktail_price * number_of_cocktails
    if current_income % 2 != 0:
        current_income = current_income * 0.75
    else:
        current_income = current_income
    total_income += current_income

    if total_income >= desired_income:
        target = True
        break
    cocktail_name = input()
if target == False:
    print(f'We need {desired_income - total_income:.2f} leva more.')
if target == True:
    print('Target acquired.')

print(f'Club income - {total_income:.2f} leva.')