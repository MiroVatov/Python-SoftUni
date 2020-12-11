n = int(input())
evens = []
odds = []
positive = []
negative = []

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        evens.append(num)
    elif num % 2 != 0:
        odds.append(num)
    if num >= 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)

command = input()

if command == 'even':
    print(evens)
elif command == 'odd':
    print(odds)
elif command == 'positive':
    print(positive)
elif command == 'negative':
    print(negative)