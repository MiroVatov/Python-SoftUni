text_messaging = input().split()

text = input()
text = [t.split() for t in text]
new_text = []
for i in text_messaging:

    sum_message = [int(i) for i in i]
    sum_message = sum(map(int, sum_message))
    for x in text:
        if sum_message > len(text):
            text_index = sum_message - len(text)
            new_index = text[text_index]
            new_text.append(new_index)
            text.remove(new_index)
            break
        else:
            new_index = text[sum_message]
            new_text.append(new_index)
            text.remove(new_index)
            break

outlst = [' '.join([str(c) for c in lst]) for lst in new_text]
final_text = ''.join(outlst)

print(final_text)
