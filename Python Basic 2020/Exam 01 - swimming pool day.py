import math
people = int(input())
entrance_fee = float(input())
lounge = float(input())
umbrella_fee = float(input())

lounge_price = math.ceil(people * 0.75)
lounge_price = lounge_price * lounge
umbrellas_fee = math.ceil(people * 0.50)
umbrellas_fee = umbrellas_fee * umbrella_fee
total_fees = (entrance_fee * people) + lounge_price + umbrellas_fee
print(f'{total_fees:.2f} lv.')