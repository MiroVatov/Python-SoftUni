age = int(input())
washing_mashine = float(input())
toy_price = int(input())
total_bday_money = 0
total_toys_price = 0
saved_money = 0
bday_money = 10

for i in range(1, age + 1):

    if i % 2 != 0:
        total_toys_price = total_toys_price + toy_price
    else:

        total_bday_money = (total_bday_money + bday_money) - 1
        bday_money = bday_money + 10

saved_money = total_toys_price + total_bday_money
left_money = abs(saved_money - washing_mashine)

if saved_money >= washing_mashine:
    print(f'Yes! {left_money:.2f}')
else:
    print(f'No! {left_money:.2f}')