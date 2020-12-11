deciphered_skill = input()

while True:
    command = input()
    if command == 'For Azeroth':
        break
    command = command.split()
    if command[0] in ['GladiatorStance', 'DefensiveStance', 'Dispel']:
        action = command[0]
        if action == 'GladiatorStance':
            deciphered_skill = deciphered_skill.upper()
            print(deciphered_skill)

        elif action == 'DefensiveStance':
            deciphered_skill = deciphered_skill.lower()
            print(deciphered_skill)

        elif action == 'Dispel':
            index = int(command[1])
            letter = command[2]
            deciphered_skill = list(deciphered_skill)
            if 0 <= index < len(deciphered_skill):
                deciphered_skill.pop(index)
                deciphered_skill.insert(index, letter)
                print(f"Success!")
            else:
                print(f"Dispel too weak.")
            deciphered_skill = ''.join(deciphered_skill)
    elif command[0] + ' ' + command[1] == 'Target Change' or command[0] + ' ' + command[1] == 'Target Remove':
        action = command[0] + ' ' + command[1]

        if action == 'Target Change':
            subst = command[2]
            second_text = command[3]
            if subst in deciphered_skill:
                deciphered_skill = deciphered_skill.replace(subst, second_text)
                print(deciphered_skill)

        elif action == 'Target Remove':
            subst = command[2]
            if subst in deciphered_skill:
                deciphered_skill = deciphered_skill.replace(subst, '', 1)
                print(deciphered_skill)

    else:
        print(f"Command doesn't exist!")