heroes_dict = {}

while True:
    command = input().split()
    if command[0] == "End":
        break

    action = command[0]
    hero_name = command[1]
    if action == "Enroll":
        if hero_name not in heroes_dict:
            heroes_dict[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")

    elif action == "Learn":
        spell_name = command[2]  # check if the spell name is made of more than one word -> split correclty
        if hero_name not in heroes_dict:
            print(f"{hero_name} doesn't exist.")
        elif hero_name in heroes_dict:
            if spell_name in heroes_dict[hero_name]:
                print(f"{hero_name} has already learnt {spell_name}.")
            else:
                heroes_dict[hero_name].append(spell_name)

    elif action == "Unlearn":
        spell_name = command[2]  # check if the spell name is made of more than one word -> split correclty
        if hero_name not in heroes_dict:
            print(f"{hero_name} doesn't exist.")
        elif hero_name in heroes_dict:
            if spell_name not in heroes_dict[hero_name]:
                print(f"{hero_name} doesn't know {spell_name}.")
            else:
                heroes_dict[hero_name].remove(spell_name)

sorted_heroes_dict = dict(sorted(heroes_dict.items(),key=lambda x:((-len(x[1]),x[0]))))

print(f"Heroes")
for hero, spells in sorted_heroes_dict.items():
    print(f"== {hero}: {', '.join(spells)}")