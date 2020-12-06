budget = float(input())
product = input()
products_count = 0
total_price = 0
while product != 'Stop':
    product_price = float(input())
    if product_price > budget:
        diff = product_price - budget
        print(f'You don\'t have enough money!')
        print(f'You need {diff:.2f} leva!')
        break
    products_count += 1
    if products_count % 3 == 0:
        product_price = product_price / 2
    budget -= product_price
    total_price += product_price
    product = input()

if product == 'Stop':
    print(f'You bought {products_count} products for {total_price:.2f} leva.')