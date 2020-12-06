import sys
n = int(input())
highest_num = -sys.maxsize
total_number = 0

for i in range(0, n):
    number = int(input())

    if number > highest_num:
        highest_num = number
    total_number += number

total_number = total_number - highest_num
if highest_num == total_number:
    print('Yes')
    print(f'Sum = {total_number}')
else:
    diff = abs(total_number - highest_num)
    print('No')
    print(f'Diff = {diff}')

