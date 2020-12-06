chars = input()

my_dict = {}

for i in chars:
    if i not in my_dict:
        my_dict[i] = 0
    my_dict[i] += 1

for key, value in my_dict.items():
    if key != ' ' and key != ' ':
        print(f"{key} -> {value}")

