
first_char = ord(input())
second_char = ord(input())

text = input()

total_sum = 0

for t in text:

    if first_char < ord(t) < second_char:
        total_sum += ord(t)

print(total_sum)

