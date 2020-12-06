import re

pattern = r'\d+'

while True:
    text = input()
    if text == '':
        break
    matches = re.findall(pattern, text)
    if len(matches) == 0:
        continue

    print(' '.join(matches), end=' ')
