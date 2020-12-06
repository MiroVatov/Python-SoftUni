import math
import sys
word = input()
max_word = -sys.maxsize
most_powerful_word = ''
while word != 'End of words':
    word_power = 0
    for i in word:
        word_power += ord(i)
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' or word[0] == 'y'\
        or word[0] == 'A' or word[0] == 'E' or word[0] == 'I' or word[0] == 'O' or word[0] == 'U' or word[0] == 'Y':
        word_power = word_power * len(word)
    else:
        word_power = math.floor(word_power / len(word))
    if word_power > max_word:
        max_word = word_power
        most_powerful_word = word
    word = input()
print(f'The most powerful word is {most_powerful_word} - {max_word}')