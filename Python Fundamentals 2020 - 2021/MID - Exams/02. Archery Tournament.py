targets = [int(i) for i in input().split("|")]
collected_points = 0

while True:
    position = 0
    command = input()
    token = command.split("@")
    action = token[0]

    if command == "Game over":
        break
    if action == "Shoot Left":
        start_index = int(token[1])
        power = int(token[2])
        if start_index in range(len(targets)):
            index = (start_index - power) % len(targets)
            if targets[index] < 5:
                collected_points += targets[index]
                targets[index] = 0
            else:
                collected_points += 5
                targets[index] -= 5

    elif action == "Shoot Right":
        start_index = int(token[1])
        power = int(token[2])

        if start_index in range(len(targets)):
            index = (start_index + power) % len(targets)
            if targets[index] < 5:
                collected_points += targets[index]
                targets[index] = 0
            else:
                collected_points += 5
                targets[index] -= 5

    elif action == "Reverse":
        targets = targets[::-1]


print(f"{' - '.join(map(str,targets))}")
print(f"Iskren finished the archery tournament with {collected_points} points!")