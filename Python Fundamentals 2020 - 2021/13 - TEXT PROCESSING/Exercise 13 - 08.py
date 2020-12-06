alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

initial_text = input().split()

total_result = 0
result = 0

for i in range(len(initial_text)):
    if i == len(initial_text):
        break
    text = initial_text[i]
    first_char = text[0]
    index_letter = alphabet.index(first_char.upper()) + 1
    number = int(text[1:-1:])
    if first_char.isupper():
        result = number / index_letter

    elif first_char.islower():
        result = number * index_letter

    second_char = text[-1]
    index_letter = alphabet.index(second_char.upper()) + 1
    if second_char.isupper():
        result = result - index_letter

    elif second_char.islower():
        second_char = second_char.upper()
        result = result + index_letter

    total_result += result
print(f"{total_result:.2f}")