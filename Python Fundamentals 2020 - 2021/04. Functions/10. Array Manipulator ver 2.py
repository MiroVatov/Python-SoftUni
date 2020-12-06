
def exchange(array, ar_index):
    index = int(command_input[1])
    array1 = array[:index + 1]
    array2 = array[index + 1:]
    return array2 + array1

def max_even_index(array, ar_index):
    index_max_even_odd = []
    max_even_odd_num = 0
    index_pos = []
    max_even = [ind for ind in array if ind % 2 == 0]
    for a in max_even:
        if a >= max(max_even):
            index_max_even_odd.append(a)
            max_even_odd_num = a
    if len(index_max_even_odd) >= 1:
        index_pos = len(array) - array[::-1].index(max_even_odd_num) - 1
        return f"{index_pos}"

    elif len(index_max_even_odd) == 0:
        return f"No matches"

def max_odd_index(array, ar_index):
    index_max_even_odd = []
    max_even_odd_num = 0
    index_pos = []
    max_odd = [ind for ind in array if ind % 2 != 0]
    for a in max_odd:
        if a >= max(max_odd):
            index_max_even_odd.append(a)
            max_even_odd_num = a
    if len(index_max_even_odd) >= 1:
        index_pos = len(array) - array[::-1].index(max_even_odd_num) - 1
        return f"{index_pos}"
    elif len(index_max_even_odd) == 0:
        return f"No matches"


def min_even_index(array, ar_index):
    index_min_even_odd = []
    min_even_odd_num = 0
    index_pos = []
    if action_2 == "even":
        min_even = [ind for ind in array if ind % 2 == 0]
        for i in min_even:
            if i <= min(min_even):
                index_min_even_odd.append(i)
                min_even_odd_num = i
        if len(index_min_even_odd) >= 1:
            index_pos = len(array) - array[::-1].index(min_even_odd_num) - 1
            return f"{index_pos}"
        elif len(index_min_even_odd) == 0:
            return f"No matches"

def min_odd_index(array, ar_index):
    index_min_even_odd = []
    min_even_odd_num = 0
    index_pos = []
    min_odd = [ind for ind in array if ind % 2 != 0]
    for i in min_odd:
        if i <= min(min_odd):
            index_min_even_odd.append(i)
            min_even_odd_num = i

    if len(index_min_even_odd) >= 1:
        index_pos = len(array) - array[::-1].index(min_even_odd_num) - 1
        return f"{index_pos}"
    elif len(index_min_even_odd) == 0:
        return f"No matches"

def first_even_fn(array, ar_index, action_2):
    first_even = [i for i in array if i % 2 == 0]
    first_even = first_even[:index]
    if len(array) >= index > 0:
        return f"{first_even}"
    elif index > len(array):
        return f"Invalid count"

def first_odd_fn(array, ar_index, action_2):
    first_odd = [i for i in array if i % 2 != 0]
    first_odd = first_odd[:index]
    if len(array) >= index > 0:
        return f"{first_odd}"
    elif index > len(array):
        return f"Invalid count"

def last_even_fn(array, ar_index, action_2):
    last_even = [i for i in array if i % 2 == 0]
    last_even = last_even[-index:]
    if len(array) >= index > 0:
        return f"{last_even}"
    elif index > len(array):
        return f"Invalid count"

def last_odd_fn(array, ar_index, action_2):
    last_odd = [i for i in array if i % 2 != 0]
    last_odd = last_odd[-index:]
    if len(array) >= index > 0:
        return f"{last_odd}"
    elif index > len(array):
        return f"Invalid count"

array = input().split(' ')
array = [int(x) for x in array]

command_input = input().split(' ')

while command_input[0] != "end":
    action = command_input[0]
    if action == "exchange":
        index = int(command_input[1])
        if 0 <= index < len(array):
            array = exchange(array, index)
        else:
            print(f"Invalid index")

    elif action == "max":
        action_2 = command_input[1]
        if action_2 == "even":
            print(max_even_index(array, action_2))
        elif action_2 == "odd":
            print(max_odd_index(array, action_2))

    elif action == "min":
        action_2 = command_input[1]
        if action_2 == "even":
            print(min_even_index(array, action_2))
        elif action_2 == "odd":
            print(max_odd_index(array, action_2))

    elif action == "first":
        action_2 = command_input[2]
        index = int(command_input[1])
        if action_2 == "even":
            print(first_even_fn(array, index, action_2))
        elif action_2 == "odd":
            print(first_odd_fn(array, index, action_2))

    elif action == "last":
        action_2 = command_input[2]
        index = int(command_input[1])
        if action_2 == "even":
            print(last_even_fn(array, index, action_2))
        elif action_2 == "odd":
            print(last_odd_fn(array, index, action_2))

    command_input = input().split()

print(array)