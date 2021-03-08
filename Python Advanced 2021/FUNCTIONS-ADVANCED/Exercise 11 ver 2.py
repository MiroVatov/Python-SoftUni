def age_assignment(*args, **kwargs):
    names_dict = {}

    for name in args:
        age = kwargs[name[0]]
        names_dict[name] = age
    return names_dict


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))