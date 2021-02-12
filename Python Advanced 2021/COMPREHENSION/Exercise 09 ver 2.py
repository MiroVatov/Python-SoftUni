items_dict = {item_name: {} for item_name in input().split(', ')}

n = int(input())

for i in range(n):
    data = input().split(' - ')
    category, item = data[0], data[1]
    additional_data = data[2].split(';')
    quantity_data = additional_data[0].split(':')
    quantity = int(quantity_data[1])
    quality_data = additional_data[1].split(':')
    quality = int(quality_data[1])
    items_dict[category][item] = {'quantity': quantity, 'quality': quality}


count_all_items = 0
total_quality = 0
categories = 0

for key, value in items_dict.items():
    categories += 1
    for val in value:
        count_all_items += value[val]['quantity']
        total_quality += value[val]['quality']


print(f"Count of items: {count_all_items}")
print(f"Average quality: {total_quality / categories:.2f}")

for cat, items in items_dict.items():
    print(f"{cat} -> {', '.join([i for i in items])}")


