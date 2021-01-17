letters_dict = {}

word_input = input()

for symbol in word_input:
    if symbol not in letters_dict:
        letters_dict[symbol] = 1
    else:
        letters_dict[symbol] += 1

for let, count in sorted(letters_dict.items()):
    print(f"{let}: {count} time/s")