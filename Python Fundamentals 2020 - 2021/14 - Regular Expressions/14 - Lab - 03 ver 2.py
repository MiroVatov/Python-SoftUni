import re

regex = r"\b(?P<day>\d{2})(?P<sep>[-.\/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"

text = input()

matches = re.finditer(regex, text)

for m in matches:
    day = m.group('day')
    month = m.group('month')
    year = m.group('year')
    print(f"Day: {day}, Month: {month}, Year: {year}")