raw_activation_key = input()

while True:

    command = input().split(">>>")

    if command[0] == "Generate":
        break

    action = command[0]

    if action == "Contains":
        substring = command[1]

        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print(f"Substring not found!")

    elif action == "Flip":
        case = command[1]
        start = int(command[2])
        end = int(command[3])
        if case == "Upper":
            raw_activation_key = raw_activation_key[:start] + raw_activation_key[start:end].upper() + raw_activation_key[end::]
        elif case == "Lower":
            raw_activation_key = raw_activation_key[:start] + raw_activation_key[start:end].lower() + raw_activation_key[end::]
        print(raw_activation_key)


    elif action == "Slice":
        start = int(command[1])
        end = int(command[2])
        raw_activation_key = raw_activation_key[0: start] + raw_activation_key[end::]
        print(raw_activation_key)

print(f"Your activation key is: {raw_activation_key}")