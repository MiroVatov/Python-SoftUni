guests_num = int(input())
pass_price = float(input())
budget = float(input())
cake_price = budget * 0.10

if 10 <= guests_num <= 15:
    pass_price = pass_price * 0.85
elif 15 < guests_num <= 20:
    pass_price = pass_price * 0.80
elif guests_num > 20:
    pass_price = pass_price * 0.75

total_bill = (pass_price * guests_num) + cake_price
money_left = abs(budget - total_bill)
if budget >= total_bill:
    print(f'It is party time! {money_left:.2f} leva left.')
else:
    print(f'No party! {money_left:.2f} leva needed.')