def change_position(paint_lst, item_idx, paint_num, change_num):
    if paint_num in paint_lst:
        item_idx = paint_lst.index(paint_num)
        paint_lst[item_idx] = change_num
        return paint_lst


def hide(paint_lst, paint_num):
    if paint_num in paint_lst:
        paint_lst.remove(paint_num)
        return paint_lst


def switch(paint_lst, paint_num, swi_num):
    if paint_num in paint_lst and swi_num in paint_lst:
        ind_a = paint_lst.index(paint_num)
        ind_b = paint_lst.index(swi_num)
        paint_lst[ind_a] = swi_num
        paint_lst[ind_b] = paint_num
        return paint_lst


def insert(paint_lst, place_n, paint_num):
    if 0 < (place_n + 1) < len(paint_lst):
        paint_lst.insert(place_n + 1, paint_num)
        return paint_lst


paintings_list = [int(i) for i in input().split()]

while True:

    command = input()
    if command == "END":
        break

    token = command.split()
    action = token[0]

    if action == "Change":
        painting_num = int(token[1])
        changed_num = int(token[2])
        if painting_num in paintings_list:
            item_index = paintings_list.index(painting_num)
            change_position(paintings_list, item_index, painting_num, changed_num)

    elif action == "Hide":
        painting_num = int(token[1])
        hide(paintings_list, painting_num)

    elif action == "Switch":
        painting_num = int(token[1])
        switch_num = int(token[2])
        switch(paintings_list, painting_num, switch_num)

    elif action == "Insert":
        place = int(token[1])
        painting_num = int(token[2])
        insert(paintings_list, place, painting_num)

    elif action == "Reverse":
        paintings_list.reverse()

print(f"{' '.join(map(str, paintings_list))}")