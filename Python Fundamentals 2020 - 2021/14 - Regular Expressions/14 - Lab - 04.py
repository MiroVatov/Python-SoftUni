import re

pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
text = input()

matches = re.finditer(pattern, text)

for m in matches:
    print(m.group(0), end=' ')