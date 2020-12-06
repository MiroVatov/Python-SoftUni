import re


while True:

    command = input()
    if command == "Last note":
        break

    pattern = r'(?P<peak_name>^[A-Za-z0-9!|@|#|\$|\?]+)[=](?P<length>[0-9]+)[<]{2}(?P<hash_code>.+$)$'

    peak_name = ''
    if re.match(pattern, command):
        pattern_match = re.finditer(pattern, command)
        for m in pattern_match:
            if int(m.group('length')) == len(m.group('hash_code')):
                peak_name = [name for name in m.group('peak_name') if name.isalpha()]
                print(f"Coordinates found! {''.join(peak_name)} -> {m.group('hash_code')}")
            else:
                print(f"Nothing found!")
    else:
        print(f"Nothing found!")