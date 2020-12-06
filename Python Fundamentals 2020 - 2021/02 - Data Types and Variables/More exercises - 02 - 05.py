n = int(input())

balanced = False

last_bracket = ''

opening_brackets = 0

for i in range(n):
    letter = input().strip(' ')

    if letter == '(':
        opening_brackets += 1

        if opening_brackets == 2:
            balanced = False
            break

        if last_bracket == ')':

            balanced = True
        last_bracket = letter
    elif letter == ')':
        if opening_brackets == 0:
            balanced = False
            break
        if last_bracket == '(':
            balanced = True

        opening_brackets = 0

        last_bracket = letter
    else:
        continue

if balanced:
    print(f'BALANCED')

else:
    print(f'UNBALANCED')