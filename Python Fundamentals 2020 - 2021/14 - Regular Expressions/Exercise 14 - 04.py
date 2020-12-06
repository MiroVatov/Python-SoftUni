import re

user_pattern = r'( |^)[a-z0-9]+([\.\-_][a-z0-9]+)*'
host_pattern = r'[a-z]+(-[a-z]+)*(\.[a-z]+(-[a-z]+)*)+'
pattern = rf'{user_pattern}@{host_pattern}'

text = input()

matches = re.finditer(pattern, text)

for m in matches:
    print(f"{m[0].strip()}")