import re

initial_text = input()

mirror_words = {}
matching_words = []
pattern = re.compile(r'(?<=[@])([A-Za-z]{3,})[@]{2}([A-Za-z]{3,})(?=[@])|(?<=[#])([A-Za-z]{3,})[#]{2}([A-Za-z]{3,})(?=[#])')

for m in re.finditer(pattern, initial_text):
    matching_words.append(m.group())
    if "##" in m.group():
        if (m.group(4)[::-1] == m.group(3)) and (m.group(3)[::-1] == m.group(4)):
            mirror_words[m.group(3)] = m.group(4)
    if "@@" in m.group():
        if (m.group(2)[::-1] == m.group(1)) and (m.group(1)[::-1] == m.group(2)):
            mirror_words[m.group(1)] = m.group(2)

if len(matching_words) == 0:
    print(f"No word pairs found!")
else:
    print(f"{len(matching_words)} word pairs found!")

if len(mirror_words) == 0:
    print(f"No mirror words!")
else:
    print(f"The mirror words are:")
    counter = 0
    for k, v in mirror_words.items():
        counter += 1
        if counter == len(mirror_words):
            print(f"{k} <=> {v}")
        else:
            print(f"{k} <=> {v}", end=', ')


