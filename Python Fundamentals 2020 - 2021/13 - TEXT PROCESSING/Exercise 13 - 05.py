initial_text = input()

for idx, ele in enumerate(initial_text):
    emoticon = []
    if ele == ":":
        emoticon.append(initial_text[idx] + initial_text[idx + 1])
        print(''.join(emoticon))
