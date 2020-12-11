import re

pattern = r'^([%|\$])(?P<tag>[A-Z][a-z]{2,})\1\:\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$'

count_of_inputs = int(input())
decrypted_message = ''

for match in range(count_of_inputs):
    encrypted_message = input()

    if re.match(pattern, encrypted_message):
        matches = re.finditer(pattern, encrypted_message)
        for m in matches:
            first_letter = chr(int(m.group(3)))
            second_letter = chr(int(m.group(4)))
            third_letter = chr(int(m.group(5)))
            decrypted_message = first_letter + second_letter + third_letter
            print(f"{m.group('tag')}: {decrypted_message}")
    else:
        print(f'Valid message not found!')
