number_of_characters = int(input())
sum_of_characters = 0
for i in range(1, number_of_characters + 1):
    character = input()
    sum_of_characters += ord(character)

print(f'The sum equals: {sum_of_characters}')