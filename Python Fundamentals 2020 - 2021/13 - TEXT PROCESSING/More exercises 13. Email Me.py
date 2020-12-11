email = input()
token = email.split('@')
text_before = sum([ord(i) for i in token[0]])
text_after = sum([ord(i) for i in token[1]])

final_sum = text_before - text_after

if final_sum >= 0:
    print(f'Call her!')
else:
    print('She is not the one.')