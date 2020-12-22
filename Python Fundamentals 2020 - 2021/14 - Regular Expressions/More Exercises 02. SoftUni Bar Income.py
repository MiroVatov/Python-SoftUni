import re

pattern = r'%(?P<name>[A-Z][a-z]+)%[^\|\$\%\.]*<(?P<product>[\w]+)>[^\|\$\%\.]*\|(?P<count>\d+)\|([^\|\$\%\.]*?(?P<price>\d+\.\d+|\d+)\$)'

Total_income = 0
while True:

    command = input()
    if command == "end of shift":
        break
    matches = re.finditer(pattern, command)

    for m in matches:
        Total_income += int(m.group('count')) * float(m.group('price'))
        price = int(m.group('count')) * float(m.group('price'))
        print(f"{m.group('name')}: {m.group('product')} - {price:.2f}")
print(f"Total income: {Total_income:.2f}")

