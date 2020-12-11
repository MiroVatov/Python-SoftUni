def take_odd(initial_text):
    new_pass = ''
    for i in range(1, len(initial_text), 2):
        new_pass += initial_text[i]
    return new_pass


def cut(initial_text, idx, length):
    new_pass = initial_text[:idx] + initial_text[idx + length:]
    return new_pass


def substitute(initial_text, subtxt, substit):
    if subtxt in initial_text:
        initial_text = initial_text.replace(subtxt, substit)
        print(f"{initial_text}")
        return initial_text

    print(f"Nothing to replace!")
    return initial_text


password_text = input()

while True:
    command = input().split()

    if command[0] == "Done":
        break

    if command[0] == "TakeOdd":
        password_text = take_odd(password_text)
        print(f"{password_text}")

    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        password_text = cut(password_text, index, length)
        print(f"{password_text}")

    elif command[0] == "Substitute":
        subtext = command[1]
        substit = command[2]
        password_text = substitute(password_text, subtext, substit)

print(f"Your password is: {password_text}")