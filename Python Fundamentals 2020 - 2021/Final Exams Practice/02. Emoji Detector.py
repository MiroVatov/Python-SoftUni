from functools import reduce
import re
initial_text = input()

cool_threshold = [int(d) for d in initial_text if d.isdigit()]
cool_threshold = reduce((lambda x, y: x * y), cool_threshold)

pattern = r'::([A-Z][a-z]{2,})::|\*\*([A-Z][a-z]{2,})\*\*'

matches = re.finditer(pattern, initial_text)

emojis_list = []

for emoji in matches:
    emojis_list.append(emoji.group())

valid_emojis_list = []

for valid in emojis_list:
    current_sum = 0
    for em in valid[2:-2]:
        current_sum += ord(em)

    if current_sum > cool_threshold:
        valid_emojis_list.append(valid)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis_list)} emojis found in the text. The cool ones are:")

for v in valid_emojis_list:
    print(v)

