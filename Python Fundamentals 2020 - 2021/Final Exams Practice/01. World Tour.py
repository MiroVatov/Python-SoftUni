initial_stops = input()

while True:
    command = input()
    if command == "Travel":
        break

    token = command.split(":")
    action = token[0]

    if action == "Add Stop":
        index = int(token[1])
        text = token[2]
        if 0 <= index < len(initial_stops):
            initial_stops = initial_stops[:index] + text + initial_stops[index:]
        print(initial_stops)
    elif action == "Remove Stop":

        start = int(token[1])
        end = int(token[2])
        if 0 <= start < len(initial_stops) and 0 <= end < len(initial_stops):
            initial_stops = initial_stops[:start] + initial_stops[end+1:]
        print(initial_stops)

    elif action == "Switch":
        old_string = token[1]
        new_string = token[2]
        if old_string in initial_stops:
            initial_stops = initial_stops.replace(old_string, new_string)
        print(initial_stops)

print(f"Ready for world tour! Planned stops: {initial_stops}")