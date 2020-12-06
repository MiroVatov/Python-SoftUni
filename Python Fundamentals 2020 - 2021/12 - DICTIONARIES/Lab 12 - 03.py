
command = input()
my_dict = {}

while command != "statistics":

    tokens = command.split(":")
    product = tokens[0]
    quantity = int(tokens[1])
    if product not in my_dict:
        my_dict[product] = 0
    my_dict[product] += quantity
    command = input()

print(f"Products in stock:")

for (product, quantity) in my_dict.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(my_dict.keys())}")
print(F"Total Quantity: {sum(my_dict.values())}")




