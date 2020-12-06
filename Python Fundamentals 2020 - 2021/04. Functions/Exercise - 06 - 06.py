password = input()

first_check = False
second_check = False
final_check = False
length_pass = len(password)

if length_pass < 6 or length_pass > 10:
    print(f'Password must be between 6 and 10 characters')
else:
    first_check = True

for a in password:
    if a.isalpha():
        second_check = True
    elif a.isdigit():
        second_check = True
    else:
        second_check = False
        print(f'Password must consist only of letters and digits')
        break

digits = 0

for i in password:
    if i.isdigit():
        digits += 1
        if digits >= 2 and (i.isdigit() or i.isalpha()):
            final_check = True
for b in password:
    if (b != b.isdigit() or b != b.isalpha()) and digits < 2:
        final_check = False
        print(f'Password must have at least 2 digits')
        break
    else:
        final_check = True

if first_check and second_check and final_check:
    print(f'Password is valid')
