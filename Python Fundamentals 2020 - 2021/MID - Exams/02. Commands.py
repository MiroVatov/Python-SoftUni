commands = [int(i) for i in input().split()]

while True:
    command = input().split()
    action = command[0]
    if action == 'end':
        break
    if action != "remove":
        start = int(command[2])
        count = int(command[4])
        if action == "reverse":
            rev_array = commands[start:start + count][::-1]
            commands = commands[:start] + rev_array + commands[start + count:]
        elif action == "sort":
            sorted_array = sorted(commands[start:start + count])
            commands = commands[:start] + sorted_array + commands[start + count:]
    else:
        count = int(command[1])
        del commands[:count]


print(", ".join(map(str, commands)))