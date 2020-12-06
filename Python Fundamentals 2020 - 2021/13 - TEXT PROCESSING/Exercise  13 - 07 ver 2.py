text = input()
strength = 0
iter = 0

while iter < len(text):
    char = text[iter]

    if char == ">":
        strength += int(text[iter + 1])
    elif strength > 0:
        text = text[:iter] + text[iter + 1:]
        iter -= 1
        strength -= 1

    iter += 1

print(text)