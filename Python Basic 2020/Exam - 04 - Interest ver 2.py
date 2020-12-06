initial_sum = float(input())
months = int(input())

simple_sum = initial_sum
complex_sum = initial_sum

for i in range(1, months + 1):
    simple_sum += (0.03 * initial_sum)
    complex_sum += (0.027 * complex_sum)

print(f'Simple interest rate: {simple_sum:.2f} lv.')
print(f'Complex interest rate: {complex_sum:.2f} lv.')

if simple_sum > complex_sum:
    diff = abs(simple_sum - complex_sum)
    print(f'Choose a simple interest rate. You will win {diff:.2f} lv.')
else:
    diff = abs(simple_sum - complex_sum)
    print(f'Choose a complex interest rate. You will win {diff:.2f} lv.')