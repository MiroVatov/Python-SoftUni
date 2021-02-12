bunker = {item_name: {} for item_name in input().split(', ')}

n = int(input())

for i in range(n):
    data = input().split(' - ')
    category, item = data[0], data[1]
    additional_data = data[2].split(';')
    quantity = int(additional_data[0].split(':')[1])
    quality = int(additional_data[1].split(':')[1])
    bunker[category][item] = (quantity, quality)

total_quality = sum([sum([qu[1] for qu in val.values()]) for key, val in bunker.items()])

count_all_items = sum([sum([qu[0] for qu in val.values()]) for key, val in bunker.items()])
average_quality = total_quality / len(bunker)

print(f"Count of items: {count_all_items}")
print(f"Average quality: {average_quality:.2f}")
[print(f"{cat} -> {', '.join(bunker[cat].keys())}") for cat in bunker]
