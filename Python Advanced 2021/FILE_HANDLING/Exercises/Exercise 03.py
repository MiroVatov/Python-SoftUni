
import os

while True:
    command = input()
    if command == 'End':
        break

    token = command.split('-')
    action = token[0]

    if action == 'Create':
        file_name = token[1]

        with open(file_name, 'w') as file:
            file.write('')

    elif action == 'Add':
        file_name, content = token[1:]

        with open(file_name, 'a') as file:
            file.write(content + '\n')

    elif action == 'Replace':
        file_name, old_text, new_text = token[1:]
        is_exists = os.path.exists(file_name)

        if is_exists:

            with open(file_name, 'r') as file:
                text = file.read()
            text = text.replace(old_text, new_text)
            with open(file_name, 'w') as file:
                file.write(text)
        else:
            print('An error occurred')

    elif action == 'Delete':
        file_name = token[1]
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print('An error occurred')
