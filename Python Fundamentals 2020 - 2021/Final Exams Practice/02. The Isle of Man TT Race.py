import re

while True:

    command = input()

    pattern = r'^([#|$|%|\*|&]{1})(?P<racer_name>[A-Za-z]+)(\1)=(?P<count>[0-9]+)[!]{2}(?P<hash_code>.+$)$'

    if re.match(pattern, command):
        pattern_match = re.finditer(pattern, command)

        for m in pattern_match:
            if int(m.group('count')) == len(m.group('hash_code')):
                hash_code = [chr(ord(code) + int(m.group('count'))) for code in m.group('hash_code')]
                print(f"Coordinates found! {m.group('racer_name')} -> {''.join(hash_code)}")

                exit()
            else:
                print(f'Nothing found!')

    else:
        print(f"Nothing found!")