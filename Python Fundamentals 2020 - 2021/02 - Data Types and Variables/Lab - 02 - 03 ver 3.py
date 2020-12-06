n = int(input())

for number in range(1, n + 1):
    sum_of_digits = 0
    for num in str(number):
        sum_of_digits += int(num)
    is_special = sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11
    print(f'{number} -> {is_special}')
