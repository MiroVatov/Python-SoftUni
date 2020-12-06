message = []
action = ''

while True:
    command = input()
    if command == "end":
        break

    token = command.split()
    action = token[0]

    if action == "Chat":
        msg: str = token[1]
        message.append(msg)

    elif action == "Delete":
        msg = token[1]
        if msg in message:
            message.remove(msg)

    elif action == "Edit":
        mst_to_edit = token[1]
        edited_msg = token[2]
        edited_msg_index = message.index(mst_to_edit)
        message[edited_msg_index] = edited_msg

    elif action == "Pin":
        msg = token[1]
        if msg in message:
            pin_msg_index = message.index(msg)
            message.append(msg)
            message.remove(msg)

    elif action == "Spam":
        for item in token:
            if item != "Spam":
                message.append(item)

for i in message:
    print(i)

