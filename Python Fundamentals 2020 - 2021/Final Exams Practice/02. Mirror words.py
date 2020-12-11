import re

initial_text = input()

mirror_words = []
matching_words = []
pattern = r'(?<=[@])([A-Za-z]{3,})[@]{2}([A-Za-z]{3,})(?=[@])|(?<=[#])([A-Za-z]{3,})[#]{2}([A-Za-z]{3,})(?=[#])'
# pattern = r'(@([A-Za-z]+){3}@@([A-Za-z]+){3}@)|(#([A-Za-z]+){3}##([A-Za-z]+){3}#)'  ->  from another code, groups must be fixed
matches = re.finditer(pattern, initial_text)
# matches = re.findall(pattern, initial_text)

for m in matches:
    matching_words.append(m.group())
    if "##" in m.group():
        if (m.group(4)[::-1] == m.group(3)) and (m.group(3)[::-1] == m.group(4)):
            mirror_words.append([m.group(3), m.group(4)])

    if "@@" in m.group():
        if (m.group(2)[::-1] == m.group(1)) and (m.group(1)[::-1] == m.group(2)):
            mirror_words.append([m.group(1), m.group(2)])

if len(matching_words) == 0:
    print(f"No word pairs found!")
else:
    print(f"{len(matching_words)} word pairs found!")

if len(mirror_words) == 0:
    print(f"No mirror words!")
else:
    print(f"The mirror words are:")
    counter = 0
    for item in mirror_words:
        counter += 1
        item = ' <=> '.join(item)
        if counter == len(mirror_words):
            print(f"{item}")
        if counter < len(mirror_words):
            print(f"{item}", end=', ')