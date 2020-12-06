coffee = 1.50
water = 1.00
coke = 1.40
snacks = 2.00

drink = input()
qty = int(input())

def orders(drink: str, qty: int):

    if drink == 'coffee':
        return coffee * qty
    elif drink == 'water':
        return water * qty
    elif drink == 'coke':
        return coke * qty
    elif drink == 'snacks':
        return snacks * qty


print(f'{orders(drink, qty):.2f}')