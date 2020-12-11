n = int(input())

numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

command = input()
filtered = []

for num in numbers:
    if command == 'even' and num % 2 == 0:
        filtered.append(num)
    elif command == 'odd' and num % 2 != 0:
        filtered.append(num)
    if command == 'positive' and num >= 0:
        filtered.append(num)
    elif command == 'negative' and num < 0:
        filtered.append(num)

print(filtered)

