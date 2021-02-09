
formatted_text = input().split(', ')

for w in range(len(formatted_text)):
    if w == len(formatted_text) - 1:
        print(f"{formatted_text[w]} -> {len(formatted_text[w])}")
    else:
        print(f"{formatted_text[w]} -> {len(formatted_text[w])}", end=', ')
