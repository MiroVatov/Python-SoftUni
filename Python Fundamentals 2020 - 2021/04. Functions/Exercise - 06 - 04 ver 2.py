number = input()
number = [n for n in number]

evens = 0
odds = 0

for i in number:
    if int(i) % 2 == 0:
        evens += int(i)
    else:
        odds += int(i)

print(f'Odd sum = {odds},', end=' ')
print(f'Even sum = {evens}')