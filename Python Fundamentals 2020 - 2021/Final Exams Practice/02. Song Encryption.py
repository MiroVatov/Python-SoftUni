import re

while True:

    pattern = r'^(?P<artist>[A-Z]{1}[a-z|\'|\s]+)?:(?P<song>[A-Z|\s]+)$'

    command = input()
    if command == "end":
        break

    if re.match(pattern, command):
        pattern_match = re.finditer(pattern, command)
        for m in pattern_match:
            key = 0
            artist = m.group('artist')
            encrypted = ''
            for a in artist:
                key = len(m.group('artist'))
                if not a == ' ' and not a == "'":
                    if a.islower():
                        if (ord(a) + key) <= ord('z'):
                            encrypted += chr(ord(a) + key)
                        else:
                            key -= abs(ord(a) - ord('z'))
                            a = 'a'
                            encrypted += chr(ord(a) + key - 1)
                    elif a.isupper():
                        if (ord(a) + key) <= ord('Z'):
                            encrypted += chr(ord(a) + key)
                        else:
                            key -= abs(ord(a) - ord('Z'))
                            a = 'A'
                            encrypted += chr(ord(a) + key - 1)
                else:
                    encrypted += a
            encrypted += "@"
            song = m.group('song')
            for s in song:
                key = len(m.group('artist'))

                if s != ' ':
                    if (ord(s) + key) <= ord('Z'):
                        encrypted += chr(ord(s) + key)
                    else:
                        key -= abs(ord(s) - ord('Z'))
                        s = 'A'
                        encrypted += chr(ord(s) + key - 1)
                else:
                    encrypted += s
            print(f"Successful encryption: {encrypted}")
    else:
        print("Invalid input!")