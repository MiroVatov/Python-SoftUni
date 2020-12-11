goods_info_dict = {}

while True:
    products_data = input().split()
    if products_data[0] == 'stocked':
        break
    product = products_data[0]
    product_price = float(products_data[1])
    quantity = int(products_data[2])

    if product not in goods_info_dict:
        goods_info_dict[product] = {'product_price': product_price, 'quantity': quantity}
    else:
        goods_info_dict[product]['quantity'] += quantity
        goods_info_dict[product]['product_price'] = product_price

grand_total = 0

for pr, data in goods_info_dict.items():
    grand_total += data['product_price'] * data['quantity']

for key, value in goods_info_dict.items():
    print(f"{key}: ${value['product_price']:.2f} * {value['quantity']} = ${value['product_price'] * value['quantity']:.2f}")
print(f'------------------------------')
print(f"Grand Total: ${grand_total:.2f}")
