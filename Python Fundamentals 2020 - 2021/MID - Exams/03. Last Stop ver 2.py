paintings_list = [int(i) for i in input().split()]

command = input()

while command != "END":

    token = command.split()
    action = token[0]

    if action == "Change":
        painting_num = int(token[1])
        changed_num = int(token[2])

        if painting_num in paintings_list:
            item_index = paintings_list.index(painting_num)
            paintings_list[item_index] = changed_num

    elif action == "Hide":
        painting_num = int(token[1])
        if painting_num in paintings_list:
            paintings_list.remove(painting_num)

    elif action == "Switch":
        painting_num = int(token[1])
        switch_num = int(token[2])
        if painting_num in paintings_list and switch_num in paintings_list:
            ind_a = paintings_list.index(painting_num)
            ind_b = paintings_list.index(switch_num)
            paintings_list[ind_a] = switch_num
            paintings_list[ind_b] = painting_num

    elif action == "Insert":
        place = int(token[1]) + 1
        painting_num = int(token[2])
        if 0 < place < len(paintings_list):
            paintings_list.insert(place, painting_num)

    elif action == "Reverse":
        paintings_list.reverse()

    command = input()

print(f"{' '.join(map(str, paintings_list))}")