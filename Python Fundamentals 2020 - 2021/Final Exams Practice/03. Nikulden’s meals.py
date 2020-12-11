meals_dict = {}
unliked_meals = 0

while True:
    command = input()
    if command == 'Stop':
        break
    token = command.split('-')
    action = token[0]
    guest, meal = token[1].strip(), token[2].strip()

    if action == 'Like':
        if guest not in meals_dict:
            meals_dict[guest] = [meal]
        else:
            if meal not in meals_dict[guest]:
                meals_dict[guest].append(meal)
    elif action == 'Unlike':
        if guest in meals_dict:
            if meal in meals_dict[guest]:
                meals_dict[guest].remove(meal)
                unliked_meals += 1
            else:
                print(f'{guest} doesn\'t have the {meal} in his/her collection.')
        else:
            print(f'{guest} is not at the party.')

sorted_meals_dict = dict(sorted(meals_dict.items(), key=lambda x: (-len(x[1]), x[0])))

for g, m in sorted_meals_dict.items():
    print(f"{g}: {', '.join(m)}")
print(f"Unliked meals: {unliked_meals}")