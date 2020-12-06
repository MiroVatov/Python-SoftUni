elements = [el for el in input().split()]
moves = 0

while True:

    command = input()
    if command == "end":
        break
    else:
        pos_1, pos_2 = [int(e) for e in command.split()]
    moves += 1

    if (pos_1 == pos_2) or (pos_1 not in range(len(elements))) or (pos_2 not in  range(len(elements))):
        middle = len(elements) // 2
        elements.insert(middle, f"-{moves}a")
        elements.insert(middle, f"-{moves}a")
        print(f"Invalid input! Adding additional elements to the board")

    elif elements[pos_1] == elements[pos_2]:
        print(f"Congrats! You have found matching elements - {elements[pos_1]}!")
        ind_to_remove = [pos_1, pos_2]
        elements = [v for i, v in enumerate(elements) if i not in ind_to_remove]

    elif elements[pos_1] != elements[pos_2]:
        print(f"Try again!")

    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break
if command == "end":
    if len(elements) > 0:
        print(f"Sorry you lose :(")
        print(f"{' '.join(map(str, elements))}")