
import itertools

key_sequence = list(map(int, input().split()))

final_text = ''

while True:

    text = input()
    if text == "find":
        break

    for value, key in zip(text, itertools.cycle(key_sequence)):
        current_value = ord(value) - key
        final_text += chr(current_value)

    start = final_text.find('&') + 1
    end = final_text.find('&', start)
    treasure = final_text[start:end]
    start = final_text.find('<') + 1
    end = final_text.find('>', start)
    coordinates = final_text[start:end]
    print(f"Found {treasure} at {coordinates}")
    final_text = ''

