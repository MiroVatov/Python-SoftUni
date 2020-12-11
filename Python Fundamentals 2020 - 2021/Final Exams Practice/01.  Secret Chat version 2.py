def insert_space(mes, idx):
    mes = mes[:idx] + " " + mes[idx:]
    return mes


def reverse(mes, sub):

    mes = mes.replace(subst, '', 1)
    mes = mes + subst[::-1]
    return mes


def change_all(mes, sub, rep):
    mes = mes.replace(sub, rep)
    return mes


message = input()

while True:
    command = input()
    if command == "Reveal":
        break

    token = command.split(":|:")
    action = token[0]

    if action == "InsertSpace":
        index = int(token[1])
        message = insert_space(message, index)
        print(message)

    elif action == "Reverse":
        subst = token[1]
        if subst in message:
            message = reverse(message, subst)
            print(message)
        else:
            print("error")

    elif action == "ChangeAll":
        subst = token[1]
        replacement = token[2]
        message = change_all(message, subst, replacement)
        print(message)

print(f"You have a new text message: {message}")


