def enroll(h_dict, hero):
    if hero not in h_dict:
        h_dict[hero] = []
    else:
        print(f"{hero} is already enrolled.")
    return h_dict


def learn(h_dict, hero, spell):
    if hero not in h_dict:
        print(f"{hero} doesn't exist.")
    elif hero in h_dict:
        if spell in h_dict[hero]:
            print(f"{hero} has already learnt {spell}.")
        else:
            heroes_dict[hero].append(spell)
    return h_dict


def unlearn(h_dict, hero, spell):
    if hero not in h_dict:
        print(f"{hero} doesn't exist.")
    elif hero in h_dict:
        if spell not in h_dict[hero]:
            print(f"{hero} doesn't know {spell}.")
        else:
            heroes_dict[hero].remove(spell)
    return h_dict


heroes_dict = {}

while True:
    command = input().split()
    if command[0] == "End":
        break

    action = command[0]
    hero_name = command[1]
    if action == "Enroll":
        heroes_dict = enroll(heroes_dict, hero_name)

    elif action == "Learn":
        spell_name = command[2]  # check if the spell name is made of more than one word -> split correclty
        heroes_dict = learn(heroes_dict, hero_name, spell_name)

    elif action == "Unlearn":
        spell_name = command[2]  # check if the spell name is made of more than one word -> split correclty
        heroes_dict = unlearn(heroes_dict, hero_name, spell_name)

sorted_heroes_dict = dict(sorted(heroes_dict.items(), key=lambda x: ((-len(x[1]),x[0]))))

print(f"Heroes")
for hero, spells in sorted_heroes_dict.items():
    print(f"== {hero}: {', '.join(spells)}")