def add(bat_d, per, he, enr):
    if per not in bat_d:
        bat_d[per] = {'health': he, 'energy': enr}
    else:
        bat_d[per]['health'] += he
    return bat_d


def attack(bat_d, att, defend, dam):
    bat_d[defend]['health'] -= dam
    if bat_d[defend]['health'] <= 0:
        del bat_d[defend]
        print(f"{defend} was disqualified!")
    bat_d[att]['energy'] -= 1
    if bat_d[att]['energy'] <= 0:
        del bat_d[att]
        print(f"{att} was disqualified!")
    return bat_d


def delete(bat_d, user):
    if user == 'All':
        bat_d.clear()
    else:
        if user in bat_d:
            del bat_d[user]
    return bat_d


battles_dict = {}

while True:
    command = input()
    if command == 'Results':
        break

    token = command.split(':')
    action = token[0]
    if action == 'Add':
        person = token[1]
        health = int(token[2])
        energy = int(token[3])
        battles_dict = add(battles_dict, person, health, energy)

    elif action == 'Attack':
        attacker = token[1]
        defender = token[2]
        damage = int(token[3])
        if attacker in battles_dict and defender in battles_dict:
            battles_dict = attack(battles_dict, attacker, defender, damage)

    elif action == 'Delete':
        username = token[1]
        battles_dict = delete(battles_dict, username)

print(f"People count: {len(battles_dict)}")

sorted_dict = dict(sorted(battles_dict.items(),key=lambda x:(-x[1]['health'], x[0])))
for key, value in sorted_dict.items():
    print(f"{key} - {value['health']} - {value['energy']}")