n = int(input())

numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

command = input()
filtered = []

for num in numbers:
    filter_passes = (
        (command == 'even' and num % 2 == 0) or
        (command == 'odd' and num % 2 != 0) or
        (command == 'positive' and num >= 0) or
        (command == 'negative' and num < 0)
    )
    if filter_passes:
        filtered.append(num)

print(filtered)