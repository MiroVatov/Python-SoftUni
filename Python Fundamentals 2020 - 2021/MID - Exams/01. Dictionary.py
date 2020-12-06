words_input = input().split(" | ")
words_to_check = input().split(" | ")
final_command = input()

words_dict = {}


for w in words_input:
    token = w.split(": ")
    word = token[0]
    definition = token[1]
    if word not in words_dict:
        words_dict[word] = [definition]
    else:
        words_dict[word].append(definition)

for second_word in words_to_check:

    if second_word in words_dict:
        print(f"{second_word}")

        for k in sorted(words_dict[second_word], key=lambda x: len(x), reverse=True):
            print(f"-{k}")


if final_command == "End":
    pass
elif final_command == "List":

    for key, val in sorted(words_dict.items()):
        print(f"{key}", end='\n')
        for v in val:
            print(f"-{v}")