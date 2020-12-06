force_side_dicts = {}

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if " | " in command:
        token = command.split(" | ")
        force_side = token[0]
        force_user = token[1]

        if force_side not in force_side_dicts.keys():
            force_side_dicts[force_side] = []
            if force_user not in [x for v in force_side_dicts.values() for x in v]:
                force_side_dicts[force_side].append(force_user)
        else:
            if force_user not in [x for v in force_side_dicts.values() for x in v]:
                force_side_dicts[force_side].append(force_user)

    else:
        token = command.split(" -> ")
        force_user = token[0]
        force_side = token[1]

        current_force_side_key = ''

        for key, value in force_side_dicts.items():
            if force_user in value:
                current_force_side_key = key
                break

        if current_force_side_key != "":
            force_side_dicts[current_force_side_key].remove(force_user)

            if force_side not in force_side_dicts.keys():
                force_side_dicts[force_side] = []
            force_side_dicts[force_side].append(force_user)
        else:
            if force_side not in force_side_dicts.keys():
                force_side_dicts[force_side] = []
            force_side_dicts[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

sorted_forces_side_dict = dict(sorted(force_side_dicts.items(), key=lambda x: (-len(x[1]), x[0])))

for side, name in sorted_forces_side_dict.items():
    if len(name) == 0:
        continue
    print(f"Side: {side}, Members: {len(name)}")
    for v in sorted(name):
        print(f"! {v}")
