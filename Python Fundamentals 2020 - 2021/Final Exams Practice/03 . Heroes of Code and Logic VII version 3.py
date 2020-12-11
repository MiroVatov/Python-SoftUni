def cast_spell(h_dict, hero, mana, spell):
    if h_dict[hero][1] >= mana:
        h_dict[hero][1] -= mana
        print(f"{hero} has successfully cast {spell} and now has {h_dict[hero][1]} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell}!")
    return h_dict


def take_damage(h_dict, hero, damage, attacker):
    h_dict[hero][0] -= damage
    if h_dict[hero][0] > 0:
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {h_dict[hero][0]} HP left!")
    else:
        del h_dict[hero]
        print(f"{hero} has been killed by {attacker}!")
    return h_dict


def recharge(h_dict, hero, amount):
    if h_dict[hero][1] + amount > 200:
        current_mana_points = 200 - heroes_dict[hero][1]
        heroes_dict[hero][1] = 200
        print(f"{hero} recharged for {current_mana_points} MP!")
    else:
        heroes_dict[hero][1] += amount
        print(f"{hero} recharged for {amount} MP!")
    return h_dict


def heal(h_dict, hero, amount):
    if h_dict[hero][0] + amount > 100:
        current_hit_points = 100 - h_dict[hero][0]
        h_dict[hero][0] = 100
        print(f"{hero} healed for {current_hit_points} HP!")
    else:
        h_dict[hero][0] += amount
        print(f"{hero} healed for {amount} HP!")
    return h_dict


MAX_HIT_POINTS = 100
MAX_MANA_POINTS = 200

number_of_heroes = int(input())
heroes_dict = {}

for hero in range(number_of_heroes):
    hero_data = input().split()
    hero_name = hero_data[0]
    hit_points = int(hero_data[1])
    mana_points = int(hero_data[2])

    if hit_points <= 100 and mana_points <= 200:
        heroes_dict[hero_name] = [hit_points, mana_points]

while True:

    command = input()
    if command == "End":
        break
    token = command.split(" - ")
    action = token[0]

    if action == "CastSpell":
        hero = token[1]
        mana_needed = int(token[2])
        spell_name = token[3]

        heroes_dict = cast_spell(heroes_dict, hero, mana_needed, spell_name)

    elif action == "TakeDamage":
        hero = token[1]
        damage = int(token[2])
        attacker = token[3]

        heroes_dict = take_damage(heroes_dict, hero, damage, attacker)

    elif action == "Recharge":
        hero = token[1]
        amount = int(token[2])
        heroes_dict = recharge(heroes_dict, hero, amount)

    elif action == "Heal":
        hero = token[1]
        amount = int(token[2])

        heroes_dict = heal(heroes_dict, hero, amount)

sorted_heroes_dict = dict(sorted(heroes_dict.items(), key=lambda x: (-x[1][0], x[0])))

for key, value in sorted_heroes_dict.items():
    print(f"{key}")
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")


