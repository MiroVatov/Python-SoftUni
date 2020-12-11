def index_checker(user, start, end):
    if 0 <= start < len(user) and 0 <= end < len(user):
        return True


def password_checker(user, text):
    if text in user:
        return True


username = input()

while True:

    command = input()
    if command == "Sign up":
        break

    token = command.split()
    action = token[0]

    if action == "Case":
        case = token[1]
        if case == 'lower':
            username = username.lower()
            print(username)
        elif case == 'upper':
            username = username.upper()
            print(username)

    elif action == "Reverse":
        start_index = int(token[1])
        end_index = int(token[2])
        if index_checker(username, start_index, end_index):
            partial_text = username[start_index:end_index+1]
            print(partial_text[::-1])
        else:
            continue

    elif action == "Cut":
        subtext = token[1]
        if password_checker(username, subtext):
            username = username.replace(subtext, '', 1)
            print(username)
        else:
            print(f"The word {username} doesn't contain {subtext}.")

    elif action == "Replace":
        character = token[1]
        if password_checker(username, character):
            username = username.replace(character, '*')
            print(username)
        else:
            continue

    elif action == "Check":
        character = token[1]
        if password_checker(username, character):
            print("Valid")
        else:
            print(f"Your username must contain {character}.")
