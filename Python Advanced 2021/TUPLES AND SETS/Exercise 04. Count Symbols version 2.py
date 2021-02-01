word = tuple(input())

unique_characters = set(word)

for el in sorted(unique_characters):
    print(f'{el}: {word.count(el)} time/s')

