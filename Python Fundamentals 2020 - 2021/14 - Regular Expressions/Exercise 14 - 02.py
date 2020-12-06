import re

pattern = r'\b([_])([a-zA-Z0-9]+\b)'

text = input()

matches = re.finditer(pattern, text)
new_list = []

for m in matches:
    new_list.append(m[2])

print(','.join(new_list))