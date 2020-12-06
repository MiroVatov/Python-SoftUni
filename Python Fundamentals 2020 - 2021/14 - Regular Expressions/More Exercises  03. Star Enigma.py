import re

planets = int(input())

planets_attacked = []
planets_destroyed = []

for planet in range(planets):
    raw_message = input()
    decryption_key = [l for l in raw_message.lower() if l == 's' or l == 't' or l == 'a' or l == 'r']
    decryption_key = len(decryption_key)
    new_message = ''
    raw_message = [r for r in raw_message]

    for r in raw_message:
        val = ord(r) - decryption_key
        new_message += chr(val)

    pattern = r'@(?P<planet_name>[A-Za-z]+)[^\@\-\!\:\>]*:(?P<population>\d+)![^\@\-\!\:\>]*(?P<attack_type>[A|D])![^\@\-\!\:\>]*(?P<soldier_count>)->\d+'

    matches = re.finditer(pattern, new_message)

    for m in matches:
        if m.group('attack_type') == 'A':
            planets_attacked.append(m.group('planet_name'))
        elif m.group('attack_type') == 'D':
            planets_destroyed.append(m.group('planet_name'))

print(f"Attacked planets: {len(planets_attacked)}")
for pl in sorted(planets_attacked):
    print(f"-> {pl}")

print(f"Destroyed planets: {len(planets_destroyed)}")
for des in sorted(planets_destroyed):
    print(f"-> {des}")

