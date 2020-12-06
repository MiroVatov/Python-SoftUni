basket_price = 1.50
wreath_price = 3.80
chocolate_bunny = 7
clients_number = int(input())
total_purchases = 0
total_purchases_price = 0
for i in range(1, clients_number + 1):
    purchase = input()
    purchase_price = 0
    current_purchases = 0

    while purchase != 'Finish':
        total_purchases += 1
        if purchase == 'basket':
            purchase_price += basket_price
        elif purchase == 'wreath':
            purchase_price += wreath_price
        elif purchase == 'chocolate bunny':
            purchase_price += chocolate_bunny

        current_purchases += 1

        purchase = input()
    if current_purchases % 2 == 0:
        purchase_price = purchase_price * 0.80

    print(f'You purchased {current_purchases} items for {purchase_price:.2f} leva.')

    total_purchases_price += purchase_price
    avg_client_spendings = total_purchases_price / clients_number
print(f'Average bill per client is: {avg_client_spendings:.2f} leva.')