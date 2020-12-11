def change(txt, char, replace):
    if char in txt:
        txt = txt.replace(char, replace)
    return txt


def end(txt, part):
    if txt.endswith(part):
        print('True')
        return True
    print('False')
    return False


def find_index(txt, char):
    f_index = txt.index(char)
    return f_index


def cut(txt, start, length):
    len_txt = start + length
    txt = txt[start:len_txt]
    return txt


initial_text = input()

while True:
    command = input()
    if command == 'Done':
        break
    token = command.split()
    action = token[0]

    if action == 'Change':
        character = token[1]
        replacement = token[2]
        initial_text = change(initial_text, character, replacement)
        print(f'{initial_text}')

    elif action == 'Includes':
        text = token[1]
        if text in initial_text:
            print('True')
        else:
            print('False')

    elif action == 'End':
        text = token[1]
        if text in initial_text:
            end(initial_text, text)

    elif action == 'Uppercase':
        initial_text = initial_text.upper()
        print(initial_text)

    elif action == 'FindIndex':
        character = token[1]
        if character in initial_text:
            print(find_index(initial_text, character))

    elif action == 'Cut':
        start_index = int(token[1])
        length = int(token[2])
        idx = start_index + length
        initial_text = cut(initial_text, start_index, length)
        print(initial_text)