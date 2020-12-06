owned_tanks_list = input().split(", ")

number_of_inputs = int(input())

for tanks in range(number_of_inputs):

    command = input()
    token = command.split(", ")
    action = token[0]

    if action == "Add":
        tank_name = token[1]

        if tank_name in owned_tanks_list:
            print(f"Tank is already bought")
        else:
            print(f"Tank successfully bought")
            owned_tanks_list.append(tank_name)

    elif action == "Remove":
        tank_name = token[1]

        if tank_name in owned_tanks_list:
            print(f"Tank successfully sold")
            owned_tanks_list.remove(tank_name)
        else:
            print(f"Tank not found")

    elif action == "Remove At":
        index = int(token[1])
        if 0 <= index < len(owned_tanks_list):
            del owned_tanks_list[index]
            print(f"Tank successfully sold")
        else:
            print(f"Index out of range")

    elif action == "Insert":
        index = int(token[1])
        tank_name = token[2]
        if 0 <= index < len(owned_tanks_list):
            if tank_name in owned_tanks_list:
                print(f"Tank is already bought")

            elif tank_name not in owned_tanks_list:
                owned_tanks_list.insert(index, tank_name)
                print(f"Tank successfully bought")
        else:
            print(f"Index out of range")

print(f', '.join(owned_tanks_list))



