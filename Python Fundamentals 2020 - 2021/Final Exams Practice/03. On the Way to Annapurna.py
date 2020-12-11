
stores_dict = {}

while True:
    command = input()
    if command == "END":
        break
    token = command.split("->")
    action = token[0]

    if action == "Add":
        store_name = token[1]
        items_lst = token[2].split(",")
        if store_name not in stores_dict:
            stores_dict[store_name] = items_lst
        else:
            stores_dict[store_name] += items_lst

    elif action == "Remove":
        store_name = token[1]
        if store_name in stores_dict:
            del stores_dict[store_name]

sorted_stores_dict = dict(sorted(stores_dict.items(), key=lambda x: (len(x[1]), x[0]),reverse=True))

print(f"Stores List:")
for store, item in sorted_stores_dict.items():
    print(f"{store}")
    for i in item:
        print(f"<<{i}>>")