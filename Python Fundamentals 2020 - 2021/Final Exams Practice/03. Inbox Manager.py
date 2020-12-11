emails_dict = {}

while True:
    command = input()
    if command == 'Statistics':
        break
    token = command.split('->')
    action = token[0]

    if action == 'Add':
        username = token[1]
        if username in emails_dict:
            print(f'{username} is already registered')

        else:
            emails_dict[username] = []
    elif action == 'Send':
        username = token[1]
        email = token[2]
        emails_dict[username].append(email)

    elif action == 'Delete':
        username = token[1]
        if username in emails_dict:
            del emails_dict[username]
        else:
            print(f'{username} not found!')

print(f'Users count: {len(emails_dict)}')
sorted_dict = dict(sorted(emails_dict.items(), key=lambda x: (-len(x[1]), x[0])))
for user, emails in sorted_dict.items():
    print(f'{user}')
    for em in emails:
        print(f' - {em}')
