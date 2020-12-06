initial_text = input()

ascii_text = [ord(ele) for sub in initial_text for ele in sub]

# for ele in initial_text:
#     ascii_text.extend((ord(num) for num in ele))

forward_text = []

for pos in ascii_text:
    forward_text.append(pos + 3)

final_text = [chr(a) for a in forward_text]

print(''.join(final_text))