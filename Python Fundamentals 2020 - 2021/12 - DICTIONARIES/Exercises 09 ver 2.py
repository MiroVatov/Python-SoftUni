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
    elif " -> " in command:
        token = command.split(" -> ")
        force_user = token[0]
        force_side = token[1]

        if force_user in [x for v in force_side_dicts.values() for x in v]:
            if force_side not in force_side_dicts.keys():
                force_side_dicts[force_side] = []
            current_force_side_key = [k for k, v in force_side_dicts.items() for n in v if ''.join(n) == force_user]
            force_side_dicts[''.join(current_force_side_key)].remove(force_user)
            force_side_dicts[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")
        else:
            if force_side not in force_side_dicts.keys():
                force_side_dicts[force_side] = []
                force_side_dicts[force_side].append(force_user)
                print(f"{force_user} joins the {force_side} side!")
            else:
                force_side_dicts[force_side].append(force_user)
                print(f"{force_user} joins the {force_side} side!")

sorted_forces_side_dict = dict(sorted(force_side_dicts.items(), key=lambda x: (-len(x[1]),x[0])))

for side, name in sorted_forces_side_dict.items():
    if len(name) == 0:
        continue
    print(f"Side: {side}, Members: {len(name)}")
    for v in sorted(name):
        print(f"! {v}")

# for key, value in force_side_dicts.items():
            #     for v in value:
            #         if ''.join(value) == force_user:
            #             current_force_side_key = key