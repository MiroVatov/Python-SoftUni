word = input().lower()


final_counter = 0
counter = 0
while "Sand".lower() in word:

    counter += 1
    if counter == word.count('sand'):
        final_counter += counter
        break
counter = 0
while "Water".lower() in word:

    counter += 1
    if counter == word.count('water'):
        final_counter += counter
        break
counter = 0
while "Fish".lower() in word:

    counter += 1
    if counter == word.count('fish'):
        final_counter += counter
        break
counter = 0
while "Sun".lower() in word:

    counter += 1
    if counter == word.count('sun'):
        final_counter += counter
        break
print(final_counter)
