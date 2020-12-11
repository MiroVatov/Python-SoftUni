children_dict = {}
presents_dict = {}

while True:
    command = input()
    if command == "END":
        break

    if 'Remove' in command:
        token = command.split('->')
        child_name = token[1]
        del children_dict[child_name]

    else:
        token = command.split('->')
        child_name = token[0]
        type_of_present = token[1]
        amount = int(token[2])

        if child_name not in children_dict:
            children_dict[child_name] = amount
        else:
            children_dict[child_name] += amount

        if type_of_present not in presents_dict:
            presents_dict[type_of_present] = amount
        else:
            presents_dict[type_of_present] += amount

print(f"Children:")
for kid, quantity in sorted(children_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f"{kid} -> {quantity}")

print(f"Presents:")
for toys, quantity in presents_dict.items():
    print(f"{toys} -> {quantity}")
