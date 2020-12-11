initial_string = input()

while True:
    command = input()
    if command == 'End':
        break
    token = command.split()
    action = token[0]
    if action == 'Translate':
        char = token[1]
        replacement = token[2]
        if char in initial_string:
            initial_string = initial_string.replace(char, replacement)
        print(initial_string)

    elif action == 'Includes':
        text = token[1]
        if text in initial_string:
            print('True')
        else:
            print('False')

    elif action == 'Start':
        text = token[1]
        if initial_string.startswith(text):
            print('True')
        else:
            print('False')

    elif action == 'Lowercase':
        initial_string = initial_string.lower()
        print(initial_string)

    elif action == 'FindIndex':
        char = token[1]
        last_index_of_char = initial_string.rindex(char)
        print(last_index_of_char)

    elif action == 'Remove':
        start_index = int(token[1])
        count = int(token[2])
        first_part = initial_string[:start_index]
        final_part = initial_string[start_index+count::]
        initial_string = first_part + final_part
        print(initial_string)