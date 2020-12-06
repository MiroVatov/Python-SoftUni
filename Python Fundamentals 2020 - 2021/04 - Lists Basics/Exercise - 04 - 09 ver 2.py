
items = input().split('|')

budget = float(input())

sum_new_prices = 0
new_budget = 0
sum_old_prices = 0
total_profit = 0
bought_products_list = []

for i in items:
    tokens = i.split('->')
    cloth_type = tokens[0]
    price = float(tokens[1])
    enough_budget = False

    if cloth_type == 'Clothes' and price <= 50 and budget >= price:
        enough_budget = True

    elif cloth_type == 'Shoes' and price <= 35 and budget >= price:
        enough_budget = True
    elif cloth_type == 'Accessories' and price <= 20.50 and budget >= price:
        enough_budget = True

    if enough_budget:
        budget -= price
        sum_old_prices += price
        price = price * 1.40
        sum_new_prices += price
        bought_products_list.append(price)

total_profit = sum_new_prices - sum_old_prices
new_budget = budget + sum_new_prices


for item in bought_products_list:
    print(f'{item:.2f}', end=' ')
print()
print(f'Profit: {total_profit:.2f}')

if new_budget >= 150:
    print('Hello, France!')
else:
    print('Time to go.')


