usernames_list = input().split(", ")
valid_usernames = []
valid = True

for i in usernames_list:
    if 3 <= len(i) <= 16:
        for a in i:
            if a.isalpha() or a.isdigit() or a == "-" or a == "_":
                valid = True
            else:
                valid = False
                break
        if valid:
            valid_usernames.append(i)
            print(''.join(i))


