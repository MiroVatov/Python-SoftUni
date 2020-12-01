puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
mignion_price = 8.20
truck_price = 2

discount_amount = 0


price_of_trip = float(input())
puzzles_qty = int(input())
talking_dolls_qty = int(input())
teddy_bear_qty = int(input())
mignion_qty = int(input())
truck_qty = int(input())

toys_qty = puzzles_qty + talking_dolls_qty + teddy_bear_qty + mignion_qty + truck_qty
amount = (puzzles_qty * puzzle_price) + (talking_dolls_qty * talking_doll_price) + (teddy_bear_qty * teddy_bear_price) + (mignion_qty * mignion_price) + (truck_qty * truck_price)

if toys_qty >= 50:
    discount_amount = amount * 0.25

final_amount = amount - discount_amount

rent = final_amount * 0.10
profit = final_amount - rent
Left_amount = abs(profit - price_of_trip)


if profit >= price_of_trip:
    print(f'Yes! {Left_amount:.2f} lv left.')
elif profit < price_of_trip:
    print(f'Not enough money! {Left_amount:.2f} lv needed.')