items_dict = {key: {} for key in input().split(', ')}

while True:
    command = input()
    if command == 'End':
        break
    data = command.split('-')
    name = data[0]
    item = data[1]
    cost = int(data[2])

    if item not in items_dict[name]:
        items_dict[name].update({item: cost})

# Printing result - Version 1 ----->

# for player, value in items_dict.items():
#     items_cost = 0
#     for cost in value.items():
#         items_cost += cost[1]
#     print(f"{player} -> Items: {len(value)}, Cost: {items_cost}")

# Printing result version 2 ------->

[print(f"{name} -> Items: {len(items_dict[name])}, Cost: {sum([value[name] for name in value])}") for name, value in items_dict.items()]