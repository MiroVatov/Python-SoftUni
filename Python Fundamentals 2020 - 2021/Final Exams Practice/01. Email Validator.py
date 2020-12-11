email_to_change = input()

while True:
    command = input()
    if command == 'Complete':
        break
    token = command.split()
    action = token[0]
    if action == 'Make':
        if token[1] == 'Upper':
            email_to_change = email_to_change.upper()
            print(email_to_change)
        elif token[1] == 'Lower':
            email_to_change = email_to_change.lower()
            print(email_to_change)
    elif action == 'GetDomain':
        count = int(token[1])
        print(f'{email_to_change[-count:]}')

    elif action == 'GetUsername':
        if '@' in email_to_change:
            index = email_to_change.index('@')
            print(f'{email_to_change[:index]}')
        else:
            print(f'The email {email_to_change} doesn\'t contain the @ symbol.')

    elif action == 'Replace':
        char = token[1]
        email_to_change = email_to_change.replace(char, '-')
        print(email_to_change)

    elif action == 'Encrypt':
        ascii_text = [ord(ch) for ch in email_to_change]
        print(' '.join(map(str, ascii_text)))
