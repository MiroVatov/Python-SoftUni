
def orders(drinks, quantity):

    result = ''

    if drink == 'coffee':
        result = 1.50 * qty
    elif drink == 'water':
        result = 1.00 * qty
    elif drink == 'coke':
        result = 1.40 * qty
    elif drink == 'snacks':
        result = 2.00 * qty

    return result

drink = input()
qty = int(input())

print(f'{orders(drink, qty):.2f}')