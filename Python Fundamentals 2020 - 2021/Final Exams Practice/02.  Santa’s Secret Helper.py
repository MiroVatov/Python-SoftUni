import re

key_to_decode_with = int(input())

decrypted_messages = []

while True:
    command = input()
    name = ''
    if command == 'end':
        break
    for i in command:
        name += chr(ord(i) - key_to_decode_with)
    decrypted_messages.append(name)

pattern = r'(?<=@)(?P<child_name>[A-Za-z]+)(?P<separ>[^@|\-|\!|\:|>]+)\!(?P<behaviour>G|N)\!'

for child in range(len(decrypted_messages)):
    match = re.finditer(pattern, decrypted_messages[child])
    for m in match:
        if m.group('behaviour') == 'G':
            print(f"{m.group('child_name')}")
