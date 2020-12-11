
def pass_btw_6_and_10(password):
    if len(password) < 6 or len(password) > 10:
        return f'Password must be between 6 and 10 characters'
    return None
def only_letters_and_str(password):

    for i in password:
        if not i.isalpha() and not i.isdigit():
            return f'Password must consist only of letters and digits'

def must_have_2_digits(password):
    digits = 0

    for a in password:
        if a.isdigit():
            digits += 1
    if digits < 2:
        return f'Password must have at least 2 digits'
    return None
validation_errors = []

def validate(password):
    validators = [
                pass_btw_6_and_10,
                only_letters_and_str,
                must_have_2_digits
            ]
    for validator in validators:
        result = validator(password)
        if result is not None:
            validation_errors.append(result)
    if len(validation_errors) == 0:
        return f'Password is valid'
    else:
        return '\n'.join(validation_errors)

password = input()
result = validate(password)
print(result)







