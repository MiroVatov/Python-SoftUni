string = input()
string = list(string)
new_list = []
upper_index = 0
for i in string:

    if i.isupper():
        index = string.index(i)
        if index in new_list:
            index = upper_index
        new_list.append(index)
    upper_index += 1
print(new_list)