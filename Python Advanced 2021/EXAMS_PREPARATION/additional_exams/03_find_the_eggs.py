from collections import deque


def find_strongest_eggs(*args):
    eggs_powers, num_sub_lists = args[0], args[1]
    eggs_powers = deque(eggs_powers)
    new_eggs_list = []
    strongest_eggs = []

    for n in range(num_sub_lists):
        new_eggs_list.append([])

    while eggs_powers:
        for i in range(num_sub_lists):
            if eggs_powers:
                element = eggs_powers.popleft()
                if i % 2 == 0:
                    new_eggs_list[i].append(element)
                else:
                    new_eggs_list[i].append(element)

    egg_is_the_strongest = False

    for eggs_list in range(len(new_eggs_list)):
        middle = len(new_eggs_list[eggs_list]) // 2
        middle_egg = new_eggs_list[eggs_list][middle]

        if len(new_eggs_list[eggs_list]) == 3:
            left_egg = new_eggs_list[eggs_list][middle - 1]
            right_egg = new_eggs_list[eggs_list][middle + 1]

            if middle_egg > left_egg and middle_egg > right_egg and right_egg > left_egg:
                strongest_eggs.append(middle_egg)
        else:
            counter = 1
            left_egg = new_eggs_list[eggs_list][middle - counter]
            right_egg = new_eggs_list[eggs_list][middle + counter]
            left_egg_index = new_eggs_list[eggs_list].index(left_egg)
            right_egg_index = new_eggs_list[eggs_list].index(right_egg)

            while 0 <= left_egg_index < len(new_eggs_list[eggs_list]) and 0 <= right_egg_index < len(new_eggs_list[eggs_list]):
                left_egg = new_eggs_list[eggs_list][middle - counter]
                right_egg = new_eggs_list[eggs_list][middle + counter]

                if middle_egg > left_egg and middle_egg > right_egg and right_egg > left_egg:
                    counter += 1
                    left_egg_index -= 1
                    right_egg_index += 1
                    egg_is_the_strongest = True
                else:
                    egg_is_the_strongest = False
                    break

        if egg_is_the_strongest:
            strongest_eggs.append(middle_egg)

    return strongest_eggs

# An egg is considered "stronger" if:
# - Its value is higher than the values of the eggs to its left and right


# test = ([-1, 7, 3, 15, 2, 12], 2)
# print(find_strongest_eggs(*test))
#
# test = ([-1, 0, 2, 5, 2, 3], 2)
# print(find_strongest_eggs(*test))
#
# test = ([51, 21, 83, 52, 55], 1)
# print(find_strongest_eggs(*test))
#
test = ([-1, 7, 3, 15, 2, 12, 5, 90, 18, 1, 89, 33], 3)
print(find_strongest_eggs(*test))

# test = ([51, 21, 83, 18, 55, 90, 31, 52, 4], 3)
# print(find_strongest_eggs(*test))
#
# test = ([-1, 7, 3, 15, 2, 12, 6, 7, 8], 3)
# print(find_strongest_eggs(*test))