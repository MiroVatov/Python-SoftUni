
def chars_in_range():
    chr1 = input()
    chr2 = input()
    text = ''

    for i in range(ord(chr1) + 1, ord(chr2)):
        text += chr(i) + ' '

    return text

print(chars_in_range())