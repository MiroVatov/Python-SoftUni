flowers = input()
flowers_qty = int(input())
budget = int(input())
roses_price = 5
dahlia_price = 3.80
tulip_price: float = 2.80
narcisus_price = 3
gladiol_price = 2.50
flowers_price = 0

 
if flowers == 'Roses':
    if flowers_qty > 80:
        flowers_price = 0.90 * roses_price
    else: 
        flowers_price = roses_price
elif flowers == 'Dahlias':
    if flowers_qty > 90:
        flowers_price = 0.85 * dahlia_price
    else: 
        flowers_price = dahlia_price  
elif flowers == 'Tulips':
    if flowers_qty > 80:
        flowers_price = 0.85 * tulip_price
    else: 
        flowers_price = tulip_price 
elif flowers == 'Narcissus':
    if flowers_qty < 120:
        flowers_price = narcisus_price * 1.15
    else: flowers_price = narcisus_price
elif flowers == 'Gladiolus':
    if flowers_qty < 80:
        flowers_price = gladiol_price * 1.20
    else: 
        flowers_price = gladiol_price
Total_flower_price = flowers_price * flowers_qty
Left_amount = abs(budget - Total_flower_price)


if budget >= Total_flower_price:
    print(f'Hey, you have a great garden with {flowers_qty} {flowers} and {Left_amount:.2f} leva left.')
else:
    print(f'Not enough money, you need {Left_amount:.2f} leva more.')