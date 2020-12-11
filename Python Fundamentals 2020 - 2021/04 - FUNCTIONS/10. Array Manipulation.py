array = input().split()
array = list(map(int, array))
command = input()

while command != "end":
    token = command.split()
    action = token[0]
    if action == "exchange":
        index = int(token[1])
        if 0 <= index < len(array):
            array1 = array[:index + 1]
            array2 = array[index + 1:]
            array = array2 + array1
        else:
            print(f"Invalid index")

    elif action == "max":
        action_2 = token[1]
        index_max_even_odd = []
        max_even_odd_num = 0
        index_pos = []
        if action_2 == "even":

            max_even = [ind for ind in array if ind % 2 == 0]
            for a in max_even:
                if a >= max(max_even):
                    index_max_even_odd.append(a)
                    max_even_odd_num = a
            if len(index_max_even_odd) >= 1:
                index_pos = len(array) - array[::-1].index(max_even_odd_num) - 1
                print(f"{index_pos}")

            elif len(index_max_even_odd) == 0:
                print(f"No matches")

        elif action_2 == "odd":

            max_odd = [ind for ind in array if ind % 2 != 0]
            for a in max_odd:
                if a >= max(max_odd):
                    index_max_even_odd.append(a)
                    max_even_odd_num = a
            if len(index_max_even_odd) >= 1:
                index_pos = len(array) - array[::-1].index(max_even_odd_num) - 1
                print(f"{index_pos}")
            elif len(index_max_even_odd) == 0:
                print(f"No matches")

    elif action == "min":
        action_2 = token[1]
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
                print(f"{index_pos}")
            elif len(index_min_even_odd) == 0:
                print(f"No matches")

        elif action_2 == "odd":
            min_odd = [ind for ind in array if ind % 2 != 0]
            for i in min_odd:
                if i <= min(min_odd):
                    index_min_even_odd.append(i)
                    min_even_odd_num = i

            if len(index_min_even_odd) >= 1:
                index_pos = len(array) - array[::-1].index(min_even_odd_num) - 1
                print(f"{index_pos}")
            elif len(index_min_even_odd) == 0:
                print(f"No matches")

    elif action == "first":
        if token[2] == "even":
            index = int(token[1])
            first_even = [i for i in array if i % 2 == 0]
            first_even = first_even[:index]
            if len(array) >= index > 0:
                print(f"{first_even}")
            elif index > len(array):
                print(f"Invalid count")

        elif token[2] == "odd":
            index = int(token[1])
            first_odd = [i for i in array if i % 2 != 0]
            first_odd = first_odd[:index]
            if len(array) >= index > 0:
                print(f"{first_odd}")
            elif index > len(array):
                print(f"Invalid count")

    elif action == "last":
        index = int(token[1])
        if token[2] == "even":
            last_even = [i for i in array if i % 2 == 0]
            last_even = last_even[-index:]
            if len(array) >= index > 0:
                print(f"{last_even}")
            elif index > len(array):
                print(f"Invalid count")

        elif token[2] == "odd":
            last_odd = [i for i in array if i % 2 != 0]
            last_odd = last_odd[-index:]
            if len(array) >= index > 0:
                print(f"{last_odd}")
            elif index > len(array):
                print(f"Invalid count")
    command = input()

print(f"{array}")
