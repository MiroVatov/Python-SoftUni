single_string = input()

digits = []
letters = []
other = []

for i in single_string:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        letters += i
    else:
        other += i

print(''.join(digits))
print(''.join(letters))
print(''.join(other))