import re

pattern = r'>>(?P<items>[A-Z|a-z]+)<<?(?P<price>\d+\.\d+|\d+)!(?P<quantity>\d+)'

products_list = []
total_money_spent = 0

while True:

    command = input()
    if command == "Purchase":
        break
    matches = re.match(pattern, command)
    if matches is None:
        continue
    products_list.append(matches.group('items'))
    total_money_spent += float(matches.group('price')) * int(matches.group('quantity'))

print(f"Bought furniture:")
for i in products_list:
    print(i)

print(f"Total money spend: {total_money_spent:.2f}")
