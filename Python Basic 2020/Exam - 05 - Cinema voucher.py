voucher_price = int(input())
purchase = input()
ticket_price = 0
product_price = 0
tickets_count = 0
product_count = 0

while purchase != 'End':

    if len(purchase) > 8:
        ticket_price = ord(purchase[0]) + ord(purchase[1])
        if ticket_price > voucher_price:
            break
        tickets_count += 1
        voucher_price -= ticket_price
    elif len(purchase) <= 8:
        product_price = ord(purchase[0])
        if product_price > voucher_price:
            break
        product_count += 1
        voucher_price -= product_price

    purchase = input()

if purchase == 'End':
    print(f'{tickets_count}')
    print(f'{product_count}')
else:
    print(f'{tickets_count}')
    print(f'{product_count}')