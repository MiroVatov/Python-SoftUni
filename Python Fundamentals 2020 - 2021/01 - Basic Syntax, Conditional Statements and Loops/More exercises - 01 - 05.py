activity = input()

coffees = 0
while activity != 'END':

    if activity == 'CODING' or activity == 'DOG' or activity == 'CAT' or activity == 'MOVIE':
        coffees += 2

    elif activity == 'coding' or activity == 'dog' or activity == 'cat' or activity == 'movie':
        coffees += 1
    else:
        activity = input()
        continue
    activity = input()

if coffees > 5:
    print(f'You need extra sleep')
else:
    print(f'{coffees}')