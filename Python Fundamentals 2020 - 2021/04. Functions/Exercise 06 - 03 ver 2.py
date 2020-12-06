
def chars_in_range(char1, char2):

    text = ''

    for i in range(chr1 + 1, chr2):
        text += chr(i) + ' '

    return text

chr1 = ord(input())
chr2 = ord(input())

res = chars_in_range(chr1, chr2)
print(res.strip())