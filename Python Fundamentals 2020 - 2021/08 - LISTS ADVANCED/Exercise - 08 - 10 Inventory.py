items_collection = input().split(", ")

command = input()

while command != "Craft!":
    token = command.split(" - ")
    action = token[0]


    if action == "Collect":
        item = token[1]
        if item not in items_collection:
            items_collection.append(item)

    elif action == "Drop":
        item = token[1]
        if item in items_collection:
            items_collection.remove(item)

    elif "Combine" in command:
        item_n = token[1].split(":")
        old_item = item_n[0]
        new_item = item_n[1]

        if old_item in items_collection:
            old_item_index = items_collection.index(old_item)
            items_collection.insert(old_item_index + 1, new_item)
    elif action == "Renew":
        item = token[1]
        if item in items_collection:
            items_collection.append(item)
            items_collection.remove(item)
    command = input()

print(f"{', '.join(items_collection)}")