def children(ch_dict, name, qty):
    if name not in ch_dict:
        ch_dict[name] = qty
    else:
        ch_dict[name] += qty
    return ch_dict


def presents(pr_dict, gift, qty):
    if gift not in pr_dict:
        pr_dict[gift] = qty
    else:
        pr_dict[gift] += qty
    return pr_dict


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

        children_dict = children(children_dict, child_name, amount)
        presents_dict = presents(presents_dict, type_of_present, amount)

print(f"Children:")
for kid, quantity in sorted(children_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f"{kid} -> {quantity}")

print(f"Presents:")
for toys, quantity in presents_dict.items():
    print(f"{toys} -> {quantity}")
