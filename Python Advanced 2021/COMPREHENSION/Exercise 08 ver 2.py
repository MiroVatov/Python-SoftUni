items_dict = {name: {} for name in input().split(', ')}

while True:
    command = input()
    if command == 'End':
        break
    data = command.split('-')
    name = data[0]
    item = data[1]
    cost = int(data[2])

    if item not in items_dict[name]:
        items_dict[name][item] = cost

[print(f"{name} -> Items: {len(items_dict[name])}, Cost: {sum(items_dict[name].values())}") for name in items_dict]