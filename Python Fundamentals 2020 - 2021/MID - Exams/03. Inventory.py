def if_exist(item, item_list):
    if item in item_list:
        return True


inventory_list = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break
    token = command.split(" - ")
    action = token[0]

    if action == "Collect":
        item_name = token[1]

        if not if_exist(item_name, inventory_list):
            inventory_list.append(item_name)
        else:
            continue
    elif action == "Drop":
        item_name = token[1]
        if if_exist(item_name, inventory_list):
            inventory_list.remove(item_name)

    elif action == "Combine Items":
        action_2 = token[1].split(":")
        old_item = action_2[0]
        new_item = action_2[1]

        if if_exist(old_item, inventory_list):
            old_item_index = inventory_list.index(old_item)
            inventory_list.insert(old_item_index + 1, new_item)
        else:
            continue
    elif action == "Renew":
        item_name = token[1]
        if if_exist(item_name, inventory_list):
            inventory_list.append(item_name)
            inventory_list.remove(item_name)


if command == "Craft!":
    print(', '.join(inventory_list))