def age_assignment(*args, **kwargs):
    names_dict = {}
    for f_letter in args:
        name = f_letter[0]
        if name in kwargs.keys():
            names_dict[f_letter] = kwargs[name]
    return names_dict


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))