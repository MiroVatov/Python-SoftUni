import re

pattern = r'(?<=\b[_]{1})[a-zA-Z0-9]+\b'

text = input()

match = re.findall(pattern, text)

print(f"{','.join(match)}")