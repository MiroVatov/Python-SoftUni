string_one = input()
string_two = input()

for i in range(len(string_one)):
    if string_one[i] != string_two[i]:
        for str_two_index in range(0, i + 1):
            print(string_two[str_two_index], end='')

        for string_one_index in range(i + 1, len(string_one)):
            print(string_one[string_one_index], end='')

        print()
