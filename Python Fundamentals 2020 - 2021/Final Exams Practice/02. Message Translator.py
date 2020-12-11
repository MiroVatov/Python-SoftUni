import re

pattern = r'!(?P<command>[A-Z][a-z]{2,})!(:)\[(?P<message>[A-Za-z]{8,})\]'

n_inputs = int(input())

for _ in range(n_inputs):
    message = input()
    encrypted_message = []
    if re.match(pattern, message):
        match = re.finditer(pattern, message)

        for w in match:
            encrypted_message = [ord(i) for i in w.group('message')]
            # for m in w.group('message'):
            #     encrypted_message.append(ord(m))
            print(f"{w.group('command')}: {' '.join(map(str, encrypted_message))}")

    else:
        print('The message is invalid')