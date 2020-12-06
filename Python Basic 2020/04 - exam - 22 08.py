initial_sum = float(input())
months  = int(input())
simple_interest = (3 * initial_sum) / 100

simple_interest_amount = initial_sum
complex_interest_amount = initial_sum

for i in range(1, months + 1):
    complex_interest = ((2.7 * complex_interest_amount) / 100)
    simple_interest_amount = simple_interest_amount + simple_interest
    complex_interest_amount = complex_interest_amount + complex_interest

print(f'Simple interest rate: {simple_interest_amount:.2f} lv.')
print(f'Complex interest rate: {complex_interest_amount:.2f} lv.')

diff = abs(simple_interest_amount - complex_interest_amount)

if simple_interest_amount > complex_interest_amount:
    print(f'Choose a simple interest rate. You will win {diff:.2f} lv.')
else:
    print(f'Choose a complex interest rate. You will win {diff:.2f} lv.')