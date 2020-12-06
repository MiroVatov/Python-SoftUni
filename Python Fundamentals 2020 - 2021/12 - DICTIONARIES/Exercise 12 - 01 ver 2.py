text = input()
my_dict = {}

for ch in text:
    if ch == " ":
        continue

    if ch in my_dict:
        my_dict[ch] += 1
    else:
        my_dict[ch] = 1

for key, value in my_dict.items():
    print(f"{key} -> {value}")