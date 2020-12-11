messages_dict = {}

capacity = int(input())

while True:
    command = input()
    if command == 'Statistics':
        break
    token = command.split('=')
    action = token[0]
    if action == 'Add':
        username = token[1]
        sent = int(token[2])
        received = int(token[3])
        if username in messages_dict:
            continue
        else:
            messages_dict[username] = {'sent': sent, 'received': received}

    elif action == 'Message':
        sender = token[1]
        receiver = token[2]
        if sender in messages_dict and receiver in messages_dict:
            if messages_dict[sender]['sent'] + messages_dict[sender]['received'] + 1 >= capacity:
                del messages_dict[sender]
                print(f'{sender} reached the capacity!')
            else:
                messages_dict[sender]['sent'] += 1
            if messages_dict[receiver]['sent'] + messages_dict[receiver]['received'] + 1 >= capacity:
                del messages_dict[receiver]
                print(f'{receiver} reached the capacity!')
            else:
                messages_dict[receiver]['received'] += 1

    elif action == 'Empty':
        username = token[1]
        if username == 'All':
            messages_dict.clear()
        else:
            if username in messages_dict:
                del messages_dict[username]
print(f'Users count: {len(messages_dict.keys())}')
sorted_dict = dict(sorted(messages_dict.items(), key=lambda x: (-x[1]['received'], x[0])))


for key, value in sorted_dict.items():
    print(f"{key} - {value['sent'] + value['received']}")