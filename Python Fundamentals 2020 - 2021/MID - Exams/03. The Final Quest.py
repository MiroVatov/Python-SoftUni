def swap(msg, w_1, w_2):
    if w_1 in msg and w_2 in msg:
        ind_1, ind_2 = msg.index(w_1), msg.index(w_2)
        msg[ind_1], msg[ind_2] = msg[ind_2], msg[ind_1]
        return msg


initial_message = input().split()

while True:
    command = input()
    if command == "Stop":
        break
    token = command.split()
    action = token[0]

    if action == "Delete":
        index = int(token[1])
        if index + 1 in range(len(initial_message)):
            initial_message.pop(index + 1)

    elif action == "Swap":
        word_1 = token[1]
        word_2 = token[2]
        swap(initial_message, word_1, word_2)

    elif action == "Put":
        word = token[1]
        index = int(token[2])
        if 0 <= index - 1 <= len(initial_message):
            initial_message.insert(index - 1, word)

    elif action == "Sort":
        initial_message = sorted(initial_message, reverse=True)

    elif action == "Replace":
        word_1 = token[1]
        word_2 = token[2]
        if word_2 in initial_message:
            ind = initial_message.index(word_2)
            initial_message[ind] = word_1

print(f"{' '.join(initial_message)}")
