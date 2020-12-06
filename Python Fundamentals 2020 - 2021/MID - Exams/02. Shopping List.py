def item_in_list(item, goods_list):
    if item in goods_list:
        return True


initial_list = input().split("!")

while True:

    command = input()

    if command == "Go Shopping!":
        break
    token = command.split()
    action = token[0]
    item = token[1]

    if action == "Urgent":
        if not item_in_list(item, initial_list):
            initial_list.insert(0, item)
        else:
            continue
    elif action == "Unnecessary":
        if item_in_list(item, initial_list):
            initial_list.remove(item)
        else:
            continue

    elif action == "Correct":
        old_item = token[1]
        new_item = token[2]

        if item_in_list(old_item, initial_list):
            index_old_item = initial_list.index(old_item)
            initial_list[index_old_item] = new_item
        else:
            continue

    elif action == "Rearrange":
        if item_in_list(item, initial_list):
            initial_list.append(item)
            initial_list.remove(item)

if command == "Go Shopping!":
    print(f"{', '.join(initial_list)}")
