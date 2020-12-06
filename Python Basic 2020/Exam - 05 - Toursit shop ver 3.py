budget = float(input())
product_name = input()
product_price = 0
total_price = 0
products_count = 0
while product_name != 'Stop':

    product_price = float(input())
    products_count += 1
    if products_count % 3 == 0:
        product_price = product_price / 2
    if product_price > budget:
        diff = product_price - budget
        print(f'You don\'t have enough money!')
        print(f'You need {diff:.2f} leva!')
        break

    total_price += product_price
    budget -= product_price
    product_name = input()
if product_name == 'Stop':
    print(f'You bought {products_count} products for {total_price:.2f} leva.')