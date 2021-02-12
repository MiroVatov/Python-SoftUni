items_dict = {item_name: {} for item_name in input().split(', ')}

n = int(input())

for _ in range(n):
    data = input().split(' - ')
    category, item = data[0], data[1]
    additional_data = data[2].split(';')
    quantity_data = additional_data[0].split(':')
    quantity = int(quantity_data[1])
    quality_data = additional_data[1].split(':')
    quality = int(quality_data[1])
    items_dict[category][item] = {'quantity': quantity, 'quality': quality}


total_quality = sum([sum([qu['quality'] for qu in val.values()]) for key, val in items_dict.items()])

count_all_items = sum([sum([qu['quantity'] for qu in val.values()]) for key, val in items_dict.items()])

# Version for calculating total_quantity and total_quality without comprehensions
#
# for key, value in items_dict.items():
#     for val in value:
#         count_all_items += value[val]['quantity']
#         total_quality += value[val]['quality']
#
#
print(f"Count of items: {count_all_items}")
print(f"Average quality: {total_quality / len(items_dict):.2f}")

[print(f"{cat} -> {', '.join(item)}") for cat, item in items_dict.items()]