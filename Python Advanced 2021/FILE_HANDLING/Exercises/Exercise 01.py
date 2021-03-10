symbols = ['-', ',', ', ', '.', '?', '!']

with open('exercise01.txt', 'r') as file:
    for index, word in enumerate(file):
        if index % 2 == 0:
            for element in symbols:
                word = word.replace(element, '@')
            text = reversed(word.split())
            print(' '.join(text))






