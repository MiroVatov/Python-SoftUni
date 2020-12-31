number_of_inputs = int(input())
empty_stack = []

for _ in range(number_of_inputs):

    command = [int(i) for i in input().split()]

    if command[0] == 1:
        element = command[1]
        empty_stack.append(element)

    elif command[0] == 2:
        if empty_stack:
            empty_stack.pop()

    elif command[0] == 3:
        if empty_stack:
            print(f"{max(empty_stack)}")

    elif command[0] == 4:
        if empty_stack:
            print(f"{min(empty_stack)}")

print(f"{', '.join(map(str, reversed(empty_stack)))}")