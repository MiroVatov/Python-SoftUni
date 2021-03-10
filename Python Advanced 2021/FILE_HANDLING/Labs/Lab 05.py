# with open('words.txt', 'w') as w:
#     w.write('quick is fault')

# with open('input.txt', 'w') as i:
#     i.write('-I was quick to judge him, but it wasn\'t his fault.\n')
#     i.write('-Is this some kind of joke?! Is it?\n')
#     i.write('-Quick, hide here…It is safer.\n')

import re

with open('words.txt') as words_fh:
    words = words_fh.read().split()


with open('input.txt') as input_fh:
    text = input_fh.read()

words_occurrences = {}

for word in words:
    matches = re.findall(rf'[\s-]({word})[\s.,?!]', text, re.MULTILINE + re.IGNORECASE)
    words_occurrences[word.lower()] = len(matches)


with open('output.txt', 'w') as output_fh:
    for word, occurrence in sorted(words_occurrences.items(), key=lambda w: -w[1]):
        print(f'{word} - {occurrence}', file=output_fh)

