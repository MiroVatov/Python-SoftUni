import re

number_of_inputs = int(input())

pattern = r'\|(?P<boss>[A-Z]{4,})\|:#(?P<title>[A-Za-z]+\s[A-Za-z]+)#'

for b in range(number_of_inputs):
    boss_data = input()
    strength = 0
    armour = 0
    if re.match(pattern, boss_data):
        match = re.finditer(pattern, boss_data)
        for m in match:
            strength = len(m.group('boss'))
            armour = len(m.group('title'))
            print(f"{m.group('boss')}, {m.group('title')}")
            print(f">>Strength: {strength}")
            print(f">>Armour: {armour}")
    else:
        print("Access denied!")