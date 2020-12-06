import re

pattern = r'www\.([a-zA-Z0-9]+)((\-[a-zA-Z0-9]+)+)?((\.[a-z]+)+(\.[a-z]+)?)'

while True:

    text = input()
    if text == '':
        break
    matches = re.finditer(pattern, text)

    for m in matches:
        print(m.group())

