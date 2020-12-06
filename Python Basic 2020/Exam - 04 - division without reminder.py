n = int(input())

nums_dividedby2 = 0
nums_dividedby3 = 0
nums_dividedby4 = 0

for i in range(1, n + 1):
    number = int(input())
    if number % 2 == 0:
        nums_dividedby2 += 1
    if number % 3 == 0:
        nums_dividedby3 += 1
    if number % 4 == 0:
        nums_dividedby4 += 1


print(f'{nums_dividedby2 / n * 100:.2f}%')
print(f'{nums_dividedby3 / n * 100:.2f}%')
print(f'{nums_dividedby4 / n * 100:.2f}%')