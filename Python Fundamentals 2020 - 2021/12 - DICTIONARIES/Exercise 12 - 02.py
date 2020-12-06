resource = input()

my_dict = {}

while resource != 'stop':
    quantity = input()

    if resource not in my_dict:
        my_dict[resource] = 0
    my_dict[resource] += int(quantity)
    resource = input()

for key, value in my_dict.items():
    print(f"{key} -> {value}")