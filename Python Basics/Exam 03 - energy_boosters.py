fruit = input()
set_size = input()
sets_ordered = int(input())
set_price = 0
set_qty = 0
if fruit == 'Watermelon' and set_size == 'small':
    set_price = 56
    set_qty = 2
elif fruit == 'Watermelon' and set_size == 'big':
    set_price = 28.70
    set_qty = 5
elif fruit == 'Mango' and set_size == 'small':
    set_price = 36.66
    set_qty = 2
elif fruit == 'Mango' and set_size == 'big':
    set_price = 19.60
    set_qty = 5
elif fruit == 'Pineapple' and set_size == 'small':
    set_price = 42.10
    set_qty = 2
elif fruit == 'Pineapple' and set_size == 'big':
    set_price = 24.80
    set_qty = 5
elif fruit == 'Raspberry' and set_size == 'small':
    set_price = 20.00
    set_qty = 2
elif fruit == 'Raspberry' and set_size == 'big':
    set_price = 15.20
    set_qty = 5
total_price = set_qty * set_price
total_price = total_price * sets_ordered

if 400 <= total_price <= 1000:
    total_price = total_price * 0.85
elif total_price > 1000:
    total_price = total_price * 0.50
print(f'{total_price:.2f} lv.')
