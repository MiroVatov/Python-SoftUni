import math
easter_bread_price = 4
egg_price = 0.45

guests_number = int(input())
budget = int(input())

total_breads = (math.ceil((guests_number / 3)) * easter_bread_price)
total_eggs = egg_price * (guests_number * 2)

total_bill = total_breads + total_eggs
breads_number = total_breads / easter_bread_price
eggs_number = total_eggs / egg_price
money_left_or_needed = abs(budget - total_bill)

if budget >= total_bill:
    print(f'Lyubo bought {int(breads_number)} Easter bread and {int(eggs_number)} eggs.')
    print(f'He has {money_left_or_needed:.2f} lv. left.')
else:
    print(f'Lyubo doesn\'t have enough money.')
    print(f'He needs {money_left_or_needed:.2f} lv. more.')


