import os


def create_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

    with open(filename, 'w') as file:
        file.write('')


def append_line_to_file(filename, content):
    if not os.path.exists(filename):
        with open(filename, 'w') as filename:
            filename.write(content + '\n')
    else:
        with open(filename, 'a') as file:
            file.write(content + '\n')


def replace_string_in_file(filename, old_text, new_text):
    is_exists = os.path.exists(filename)
    new_lines = []

    if is_exists:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                new_lines.append(line.replace(old_text, new_text))
        with open(filename, 'w') as file:
            for line in new_lines:
                file.write(line)
              # file.write(''.join(new_lines))
    else:
        print('An error occurred')


def delete_file(filename):
    # if os.path.exists(filename):
    #     os.remove(filename)
    # else:
    #     print('An error occurred')

    try:
        os.remove(filename)
    except FileNotFoundError:
        print('An error occurred')


while True:
    command = input()

    if command == 'End':
        break

    token = command.split('-')
    action = token[0]

    if action == 'Create':
        filename = token[1]
        create_file(filename)

    elif action == 'Add':
        filename, content = token[1:]
        append_line_to_file(filename, content)

    elif action == 'Replace':
        filename, old_text, new_text = token[1:]
        replace_string_in_file(filename, old_text, new_text)

    elif action == 'Delete':
        filename = token[1]
        delete_file(filename)