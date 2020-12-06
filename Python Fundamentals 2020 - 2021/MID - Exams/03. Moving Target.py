def index_validator(ind, target_list):
    if 0 <= ind < len(target_list):
        return True


targets_list = [int(x) for x in input().split()]

while True:

    command = input()
    if command == "End":
        break
    token = command.split()
    index = int(token[1])

    if token[0] == "Shoot":
        power = int(token[2])

        if index_validator(index, targets_list):
            target_index = targets_list[index]
            targets_list[index] -= power
            if targets_list[index] <= 0:
                targets_list.pop(index)


    elif token[0] == "Add":
        power = int(token[2])
        if index_validator(index, targets_list):
            targets_list.insert(index, power)
        else:
            print(f"Invalid placement!")

    elif token[0] == "Strike":
        radius = int(token[2])
        if index_validator(index, targets_list):
            start = index - radius
            end = index + radius

            if start >= 0 and end < len(targets_list):
                del targets_list[start:end + 1]
            else:
                print(f"Strike missed!")

if command == "End":
    print(f"{'|'.join(map(str, targets_list))}")
