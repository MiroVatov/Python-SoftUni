primary_amount = float(input())
months = int(input())
complex_amount = 0
primary_amount_perc = primary_amount * 0.03
complex_amount_perc = primary_amount * 0.027

for i in range(1, months + 1):

    primary_amount = primary_amount + primary_amount_perc
    complex_amount = (primary_amount - primary_amount_perc) + complex_amount_perc

print(f'Simple interest rate: {primary_amount:.2f} lv.')
print(f'Complex interest rate: {complex_amount:.2f} lv.')

diff = abs(primary_amount - complex_amount)
if primary_amount > complex_amount:
    print(f'Choose a simple interest rate. You will win {diff:.2f} lv.')
else:
    print(f'Choose a complex interest rate. You will win {diff:.2f} lv.')