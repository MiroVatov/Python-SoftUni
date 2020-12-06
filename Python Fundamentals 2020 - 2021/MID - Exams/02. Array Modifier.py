initial_array = [int(x) for x in input().split()]

command = input()

while command != "end":
    token = command.split()
    cmd = token[0]

    if cmd == "swap":
        el_1 = int(token[1])
        el_2 = int(token[2])
        initial_array[el_1], initial_array[el_2] = initial_array[el_2], initial_array[el_1]
    elif cmd == "multiply":
        el_1 = int(token[1])
        el_2 = int(token[2])
        initial_array[el_1] = initial_array[el_1] * initial_array[el_2]
    elif cmd == "decrease":
        initial_array = [x - 1 for x in initial_array]
    command = input()
#print(f"{str(initial_array)[1:-1]}")
print(', '.join(map(str, initial_array)))