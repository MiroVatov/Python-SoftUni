first_string = input()
second_string = input()

changed_string = list(first_string)

for char in range(len(first_string)):
    if first_string[char] != second_string[char]:
        changed_string[char] = second_string[char]
        print("".join(changed_string))
