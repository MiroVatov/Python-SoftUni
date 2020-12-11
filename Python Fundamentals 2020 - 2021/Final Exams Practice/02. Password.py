import re

number_of_passwords = int(input())

for p in range(number_of_passwords):

    pattern = r'^(?P<start>.+)[>]{1}(?P<first>[\d]{3})\|(?P<second>[a-z]{3})\|(?P<third>[A-Z]{3})\|(?P<fourth>[^<>]{3})[<]{1}(?P=start)$'

    password = input()

    encrypted_password = ''

    if re.match(pattern, password):
        pattern_match = re.finditer(pattern, password)
        for m in pattern_match:
            encrypted_password = m.group('first') + m.group('second') + m.group('third') + m.group('fourth')
            print(f"Password: {encrypted_password}")
    else:
        print(f"Try another password!")
