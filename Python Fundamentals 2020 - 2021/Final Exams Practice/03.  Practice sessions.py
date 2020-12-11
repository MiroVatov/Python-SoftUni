roads_dict = {}

while True:
    command = input()

    if command == "END":
        break
    token = command.split("->")
    action = token[0]

    if action == "Add":
        road = token[1]
        racer = token[2]
        if road not in roads_dict:
            roads_dict[road] = [racer]
        else:
            roads_dict[road] += [racer]

    elif action == "Move":
        current_road = token[1]
        racer = token[2]
        next_road = token[3]
        if racer in roads_dict[current_road]:
            roads_dict[next_road] += [racer]
            roads_dict[current_road].remove(racer)
    elif action == "Close":
        road = token[1]
        if road in roads_dict:
            del roads_dict[road]

sorted_roads_dict = dict(sorted(roads_dict.items(),key=lambda x: (-len(x[1]), x[0])))

print(f"Practice sessions:")
for k, v in sorted_roads_dict.items():
    print(f"{k}")
    for racer in v:
        print(f"++{racer}")