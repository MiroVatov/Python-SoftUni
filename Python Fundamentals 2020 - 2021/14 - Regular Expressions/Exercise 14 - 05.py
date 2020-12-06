import re
import itertools

pattern = r'>>([A-Z|a-z]+)<<?(\d+\.\d+|\d+)!(\d+)'

products_list = []
prices_list = []
quantity = []

while True:

    command = input()
    if command == "Purchase":
        break
    matches = re.finditer(pattern, command)
    for m in matches:
        products_list.append(m.group(1))
        prices_list.append(m.group(2))
        quantity.append(m.group(3))

print(f"Bought furniture:")
for i in products_list:
    print(i)

prices_list = [float(p) for p in prices_list]
quantity = [int(q) for q in quantity]

total_money_spent = 0

for p, q in itertools.zip_longest(prices_list, quantity):
    total_money_spent += p * q

print(f"Total money spend: {total_money_spent:.2f}")