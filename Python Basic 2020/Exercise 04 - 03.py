import sys
n = int(input())

odd_sum = 0
odd_sum_min = sys.maxsize
odd_sum_max = -sys.maxsize
even_sum = 0
even_sum_min = sys.maxsize
even_sum_max = -sys.maxsize

for i in range(1, n + 1):
    number = float(input())
    if i % 2 != 0:
        odd_sum += number
        if  number < odd_sum_min:
            odd_sum_min = number
        if number > odd_sum_max:
            odd_sum_max = number

    else:
        even_sum += number
        if number < even_sum_min:
            even_sum_min = number
        if number > even_sum_max:
            even_sum_max = number

print(f'OddSum={odd_sum:.2f},')

if odd_sum_min != sys.maxsize:
    print(f'OddMin={odd_sum_min:.2f},')
else:
    print(f'OddMin=No,')
if odd_sum_max != -sys.maxsize:
    print(f'OddMax={odd_sum_max:.2f},')
else:
    print(f'OddMax=No,')

print(f'EvenSum={even_sum:.2f},')

if even_sum_min != sys.maxsize:
    print(f'EvenMin={even_sum_min:.2f},')
else:
    print(f'EvenMin=No,')
if even_sum_max != -sys.maxsize:
    print(f'EvenMax={even_sum_max:.2f}')
else:
    print(f'EvenMax=No')