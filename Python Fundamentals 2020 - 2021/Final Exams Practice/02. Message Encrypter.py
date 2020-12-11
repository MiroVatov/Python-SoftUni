import re

pattern = r'([\*|@])(?P<tag>[A-Z][a-z]{2,})\1\:\s\[([A-Za-z]+)\]\|\[([A-Za-z]+)\]\|\[([A-Za-z]+)\]\|$'

count_of_inputs = int(input())
decrypted_message = ''

for match in range(count_of_inputs):
    encrypted_message = input()
    ''''
    re.match() searches only from the beginning of the string and return match object if found. But if a match of substring is found somewhere in the middle of the string, it returns none. 
    While re.search() searches for the whole string even if the string contains multi-lines and tries to find a match of the substring in all the lines of string.
    Both re.search() and re.match() returns only the first occurrence of a substring in the string and ignore others. 
    '''
    if re.search(pattern, encrypted_message):
        matches = re.finditer(pattern, encrypted_message)
        for m in matches:
            first_num = ord((m.group(3)))
            second_num = ord((m.group(4)))
            third_num = ord((m.group(5)))

            print(f"{m.group('tag')}: {first_num} {second_num} {third_num}")
    else:
        print(f'Valid message not found!')
