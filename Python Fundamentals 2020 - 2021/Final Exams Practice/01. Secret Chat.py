message = input()

while True:
    command = input()
    if command == "Reveal":
        break

    token = command.split(":|:")
    action = token[0]

    if action == "InsertSpace":
        index = int(token[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif action == "Reverse":
        subst = token[1]
        if subst in message:
            message = message.replace(subst, '', 1)
            message = message + subst[::-1]
            print(message)
        else:
            print("error")

    elif action == "ChangeAll":
        subst = token[1]
        replacement = token[2]
        message = message.replace(subst, replacement)
        print(message)

print(f"You have a new text message: {message}")


