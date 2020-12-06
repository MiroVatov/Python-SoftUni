initial_string = input()

explosion = ">"
total_strength = 0

for char in range(len(initial_string)):
    if char == len(initial_string):
        break
    if initial_string[char] == explosion:
        strength = initial_string[char + 1]
        if int(strength) < len(initial_string[char::]):
            next_char = initial_string[char + 2]

            if next_char == ">":

                strength = int(strength)
                if strength >= len(initial_string[char::]):

                    initial_string = initial_string.replace(initial_string[char + 1::], '', 1)
                    break
                else:
                    initial_string = initial_string.replace(initial_string[char + 1], '', 1)
                    total_strength -= 1
                    total_strength += strength
            else:

                strength = int(strength)
                if strength >= len(initial_string[char::]):
                    initial_string = initial_string.replace(initial_string[char + 1::], '', 1)
                    break
                else:
                    total_strength += strength
                    initial_string = initial_string.replace(initial_string[(char + 1):(char + 1 + total_strength)], '', 1)
                    total_strength = 0
        else:
            strength = int(strength)
            initial_string = initial_string.replace(initial_string[char + 1::], '', 1)

print(initial_string)