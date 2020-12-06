initial_text = input()

final_result = ''
partial_result = ''
rep_times = ''

for val in range(len(initial_text)):
    if initial_text[val].isdigit():
        rep_times += initial_text[val]
        continue
    elif not initial_text[val].isdigit():

        if rep_times is not '':
            partial_result *= int(rep_times)
            final_result += partial_result
            partial_result = ''
            rep_times = ''
    partial_result += initial_text[val].upper()

if rep_times.isdigit():
    final_result += (partial_result * int(rep_times))

unique_symbols = set(final_result)

print(f"Unique symbols used: {len(unique_symbols)}")
print(final_result)