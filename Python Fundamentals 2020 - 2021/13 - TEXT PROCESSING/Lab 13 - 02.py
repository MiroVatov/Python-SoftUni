list_of_strings = input().split()

# for i in list_of_strings:
#     number_of_repeats = len(i)
#     print(f"{''.join(i * number_of_repeats)}", end='')
#

result = ''

for word in list_of_strings:
    number_of_repeats = len(word)
    result += word * number_of_repeats
print(result)

